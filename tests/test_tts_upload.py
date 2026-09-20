"""Offline checks for local references and the real Requests multipart encoder."""
import io
import json
from pathlib import Path
import runpy
from types import SimpleNamespace
import tempfile
import unittest
from unittest.mock import Mock, patch
import wave
from email.parser import BytesParser
from email.policy import default

import requests

from tts_cli import tts_cloning as client
from tts_cli import voice_files


class VoiceUploadTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.root_patch = patch.object(voice_files, 'PROJECT_ROOT', self.root)
        self.root_patch.start()
        self.addCleanup(self.root_patch.stop)
        self.wav = self.root / 'voices' / 'sample.wav'
        self.wav.parent.mkdir()
        with wave.open(str(self.wav), 'wb') as audio:
            audio.setnchannels(1)
            audio.setsampwidth(2)
            audio.setframerate(22050)
            audio.writeframes(b'\0\0' * 100)
        with patch('builtins.open', return_value=io.StringIO('{"NPC": "voices/sample.wav"}')):
            self.processor = client.TTSProcessor('deDE')
        self.output_patch = patch.object(client, 'SOUND_OUTPUT_FOLDER', str(self.root / 'output'))
        self.output_patch.start()
        self.addCleanup(self.output_patch.stop)

    def test_real_multipart_encoding_and_file_id_download(self):
        seen = []

        def respond(request, **kwargs):
            seen.append(request)
            response = requests.Response()
            response.status_code = 200
            if request.method == 'POST':
                envelope = (f'Content-Type: {request.headers["Content-Type"]}\r\n\r\n'.encode()
                            + request.body)
                parts = list(BytesParser(policy=default).parsebytes(envelope).iter_parts())
                self.assertEqual(len(parts), 2)
                fields = {p.get_param('name', header='content-disposition'): p for p in parts}
                self.assertEqual(set(fields), {'request', 'file'})
                self.assertIsNone(fields['request'].get_filename())
                payload = json.loads(fields['request'].get_payload(decode=True))
                self.assertNotIn('voice_id', payload)
                self.assertEqual(payload, {
                    'text': 'Hallo', 'language': 'de', 'speed': 1.0, 'pitch': 1.0,
                    'temperature': 0.6, 'top_p': 0.65, 'top_k': 45,
                    'repetition_penalty': 10.0, 'length_penalty': 0.65,
                    'gpt_cond_len': 30, 'gpt_cond_chunk_len': 4,
                    'max_ref_len': 30, 'sound_norm_refs': False,
                })
                self.assertEqual(fields['file'].get_filename(), 'sample.wav')
                self.assertEqual(fields['file'].get_content_type(), 'audio/wav')
                self.assertEqual(fields['file'].get_payload(decode=True), self.wav.read_bytes())
                self.assertEqual(kwargs['timeout'], 300)
                response._content = b'{"file_id":"synthetic-id","file_path":"/wrong.mp3"}'
            else:
                self.assertEqual(request.url, client.TTS_BASE_URL + '/api/v1/sounds/synthetic-id')
                self.assertEqual(kwargs['timeout'], 60)
                response._content = b'synthetic-output'
            return response

        with patch.object(requests.Session, 'send', side_effect=respond):
            result = self.processor.tts('voices/sample.wav', ' Hallo ', 'quest', 'quests')
        self.assertIn('saved successfully', result)
        self.assertEqual(len(seen), 2)
        self.assertEqual((self.root / 'output/quests/quest.mp3').read_bytes(), b'synthetic-output')

    def test_invalid_references_do_not_send_requests_or_overwrite_output(self):
        invalid = self.root / 'invalid.wav'
        invalid.write_bytes(b'not WAV')
        oversized = self.root / 'large.wav'
        with oversized.open('wb') as f:
            f.truncate(voice_files.MAX_REFERENCE_BYTES + 1)
        output = self.root / 'output/quests/test.mp3'
        output.parent.mkdir(parents=True)
        output.write_bytes(b'existing')
        for name in ['missing.wav', 'legacy-id', 'invalid.wav', 'large.wav']:
            with self.subTest(name=name), patch.object(requests.Session, 'send') as send:
                result = self.processor.tts(name, 'Test', 'test', 'quests', forceGen=True)
                self.assertIn('Error:', result)
                send.assert_not_called()
                self.assertEqual(output.read_bytes(), b'existing')
        with patch.object(requests.Session, 'send') as send:
            self.assertEqual(self.processor.tts('missing.wav', 'Test', 'test', 'quests'),
                             'duplicate generation, skipping')
            send.assert_not_called()

    def test_normal_generation_and_regeneration_pass_paths(self):
        row = SimpleNamespace(name='NPC', cleanedText='Hallo', quest='1', source='accept',
                              DisplayRaceID=1, DisplaySexID=0, original_text='Hello', player_gender=None)
        with patch.object(self.processor, 'tts') as tts, patch.object(self.processor, '_get_output_target', return_value=('quests', '1-accept')):
            self.processor.tts_row(row)
            self.assertEqual(tts.call_args.args[0], 'voices/sample.wav')
            self.processor._regenerate_from_entry(vars(row) | {'text': 'Hallo'})
            self.assertEqual(tts.call_args.kwargs['voice_path'], 'voices/sample.wav')
            self.assertTrue(tts.call_args.kwargs['forceGen'])

    def test_switch_validates_before_saving_and_matches_equivalent_paths(self):
        with patch.object(self.processor, '_load_voice_clone_map', return_value={'NPC': 'voices/sample.wav'}), patch.object(self.processor, '_save_voice_clone_map') as save:
            with self.assertRaises(FileNotFoundError):
                self.processor.switch_voice(str(self.wav), 'missing.wav')
            save.assert_not_called()
        replacement = self.root / 'replacement.wav'
        replacement.write_bytes(self.wav.read_bytes())
        with patch.object(self.processor, '_load_voice_clone_map', return_value={'NPC': 'voices/sample.wav'}), patch.object(self.processor, '_save_voice_clone_map') as save, patch.object(self.processor, 'regenerate_for_npc') as regenerate:
            self.processor.switch_voice(str(self.wav), 'replacement.wav')
            save.assert_called_once_with({'NPC': 'replacement.wav'})
            self.assertEqual(self.processor.voiceCloneMap['NPC'], 'replacement.wav')
            regenerate.assert_called_once_with('NPC')

    def test_regenerate_by_voice_matches_resolved_path_and_refreshes_map(self):
        with patch.object(self.processor, '_load_voice_clone_map_json', return_value={'New NPC': 'voices/sample.wav'}), patch.object(self.processor, 'regenerate_for_npc') as regenerate:
            self.processor.regenerate_all_with_voice(str(self.wav))
            regenerate.assert_called_once_with('New NPC')
            self.assertEqual(self.processor.voiceCloneMap, {'New NPC': 'voices/sample.wav'})

    def test_directory_generator_keeps_wav_extension_and_excludes_other_files(self):
        script = Path(client.__file__).resolve().parent.parent / 'create-voice-clone-map.py'
        module = runpy.run_path(str(script))
        select = module['select_random_voice']
        select.__globals__['BASE_DIR'] = str(self.root)
        directory = self.root / 'de/human'
        directory.mkdir(parents=True)
        (directory / 'm-example.WAV').write_bytes(self.wav.read_bytes())
        (directory / 'm-ignore.mp3').write_bytes(b'mp3')
        self.assertEqual(select('de', 'human', 'male'), 'de/human/m-example.WAV')

    def test_export_generator_writes_existing_paths_and_preserves_map_if_missing(self):
        reference = self.root / 'refs/quests/1-accept.wav'
        reference.parent.mkdir(parents=True)
        reference.write_bytes(self.wav.read_bytes())
        fixtures = {
            './sql.json': [{'name': 'NPC', 'source': 'accept', 'quest': '1',
                            'DisplayRaceID': 1, 'DisplaySexID': 0}],
            './gossip.json': {}, './sound_length.json': {'1-accept': 10},
        }
        output = self.root / 'map.json'
        original_open = open

        def open_fixture(path, mode='r', **kwargs):
            if mode == 'r':
                return io.StringIO(json.dumps(fixtures[path]))
            self.assertEqual(path, 'voice-clone-map.json')
            return original_open(output, mode, **kwargs)

        with patch.object(client, 'SOUND_INPUT_FOLDER', 'refs'), patch('builtins.open', side_effect=open_fixture):
            client.create_voice_clone_map()
            self.assertEqual(json.loads(output.read_text()), {'NPC': 'refs/quests/1-accept.wav'})
            reference.unlink()
            with self.assertRaisesRegex(ValueError, 'No local WAV references'):
                client.create_voice_clone_map()
            self.assertEqual(json.loads(output.read_text()), {'NPC': 'refs/quests/1-accept.wav'})

    def test_failed_synthesis_or_missing_id_never_downloads(self):
        with patch.object(client.requests, 'post') as post, patch.object(client.requests, 'get') as get:
            post.side_effect = requests.exceptions.ConnectionError('synthetic failure')
            result = self.processor.tts('voices/sample.wav', 'Test', 'test', 'quests')
            self.assertIn('unable to generate audio', result)
            get.assert_not_called()
            post.side_effect = None
            post.return_value = Mock(json=Mock(return_value={'file_path': '/wrong.mp3'}))
            result = self.processor.tts('voices/sample.wav', 'Test', 'test', 'quests')
            self.assertIn('No file_id', result)
            get.assert_not_called()
            self.assertFalse((self.root / 'output/quests/test.mp3').exists())


if __name__ == '__main__':
    unittest.main()
