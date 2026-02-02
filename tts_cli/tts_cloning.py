import os
import pandas as pd
from tqdm import tqdm
import hashlib
from concurrent.futures import ThreadPoolExecutor
import re
from tts_cli.consts import RACE_DICT, GENDER_DICT
from tts_cli.length_table import write_sound_length_table_lua
from tts_cli.utils import get_first_n_words, get_last_n_words, replace_dollar_bs_with_space
from slpp import slpp as lua
from pydub import AudioSegment
import json
import random
from concurrent.futures import ProcessPoolExecutor, as_completed
from tqdm import tqdm
import math
import requests
import shutil

# TODO: make module name a cli arg when we do other expansions
MODULE_NAME = 'AI_VoiceOverData_Vanilla'
OUTPUT_FOLDER = MODULE_NAME + '/generated'
SOUND_OUTPUT_FOLDER =  OUTPUT_FOLDER + '/sounds'
SOUND_INPUT_FOLDER = OUTPUT_FOLDER + '/input-sounds'
DATAMODULE_TABLE_GUARD_CLAUSE = 'if not VoiceOver or not VoiceOver.DataModules then return end'
# TODO: use replace map for each language.
REPLACE_DICT = {
    # Placeholder
    '$nath,': '$n,',
    '$B $B': '',
    '$b': '\n',
    '$B': '\n',
    '$n': 'Abenteurer',
    '$N': 'Abenteurer',
    '$C': 'Champion',
    '$c': 'Champion',
    '$R': 'Reisender',
    '$r': 'Reisender',

    # Cities & Zones
    'Stormwind': 'Sturmwind',
    'Thunder Bluff': 'Donnerfels',
    'Thunderbluff': 'Donnerfels',
    'Undercity': 'Unterstadt',
    'Ironforge': 'Eisenschmiede',
    'Silvermoon': 'Silbermond',
    'Gnomeregan': 'Gnomeregahn',
    'Alterac': 'Alterak',
    'Alteractal': 'Alteraktal',
    'Arathi': 'Arati',
    'Ashenvale': 'Eschenwald',
    'Stranglethorn': 'Schlingendorntal',
    'Barrens': 'Brachland',
    'Mulgore': 'Mullgor',
    'Lordaeron': 'Lorderon',
    "Quel'Thalas": 'Quel Thalas',
    'Eastern Kingdoms': 'Östliche Königreiche',
    'Astranaar': 'Astranahr',
    'Coldridge-Tal': 'Coldridge-Tahl',
    'Azeroth': 'Azerott',

    # Dungeons & Raids
    'Ragefire Chasm': 'Flammenschlund',
    'Ragefireabgrund': 'Flammenschlund',
    'Deadmines': 'Todesminen',
    'Wailing Caverns': 'Die Höhlen des Wehklagens',
    'Shadowfang Keep': 'Burg Schattenfang',
    'Blackfathom Deeps': 'Tiefschwarze Grotte',
    'Scarlet Monastery': 'Scharlachrotes Kloster',
    'Stratholme': 'Stratholm',
    'Molten Core': 'Geschmolzener Kern',
    'Blackwing Lair': 'Pechschwingenhort',

    # NPC Names
    'Bronzebeard': 'Bronzebart',
    'Stormrage': 'Sturmgrim',
    'Whisperwind': 'Flüsterwind',
    'Hellscream': 'Höllschrei',
    'Windrunner': 'Windläufer',
    'Grual': 'Gru-al',
    'Dendrite': 'Dendrit',
    'Starblaze': 'ßtahrblaiß',
    'Greywhisker': 'Gräiwisker',

    # Races
    'Night Elf': 'Nachtelf',
    'Blood Elf': 'Blutelf',
    'Undead': 'Untoter',
    'Forsaken': 'Die Verlassenen',
    'Dwarf': 'Zwerg',

    # Wording
    'Rowdys': 'Raudis',
    'SI:7.': 'S-I-7,',
    'SI:7': 'S-I-7',
    'Stonemaulklan': 'Stohnmaulklan',
    'Dustwallow': 'Dahstwolloh',
    'Moonglade': 'Muhnglehd',
    'Elissa Starbreeze': 'Ilissa Stahrbries',
    'Cliffspring': 'Kliff s\'pring',
    'bitte schön': 'bitteschön',
    'Oh-ho!': 'Oho!',
    'un... un... unhygienisch!': 'un. un. unhygienisch!',
    'Der Goldküstensteinbruch befindet sich in der Nähe der Küste, westlich vom Turm.': 'Der Goldküstensteinbruch befindet sich in der Nähe der Küste, westlich vom Turm..',
    'Pah!': 'Pah.',
    'Was wollt lhr von mir': 'Was wollt Ihr von mir',
    'Aghhh...': 'Aarrgh,',
    'Githyiss die Üble': 'Githyiss-die-Üble',
    ' der Defias': '-der-Defias',
    'Mathrengyl': 'Masrengil',
    'Bearwalker': 'Birwalker',
    'Entschuldigung...': 'Entschuldigung,',
    'Brzzzzt! ': '',
    'so\'n': 'son',
    'Cenarius\'': 'Cenarius',
    'Spionagebot': 'Spionage-Bott',
    'is\'': 'is',
    'Schietkram': 'Schitkram',
    'Archäologe': 'Arschheologe',
    'archäologe': 'arschheologe',
    'Hier,': 'Hier',
    'Stormpike': 'ßtohrmpaike',


    # Numbers
    '01101100': '', 
    '01001100': '', 
    '01101000': '', 
    '01001011': '', 
    '01100111': '', 
    '01110110': '', 
    '00100001': '',
    '01101101': '', 
    '01101101': '', 
    '01010100': '', 
    '01110101': '', 
    '01100110': '', 
    '01100100': '', 
    '01110000': '', 
    '01111001': '',
    '01010111': '',
    '01001110': '', 
    '01101001': '', 
    '01100101': '', 
    '01010000': '', 
    '01110010': '', 
    '01110100': '', 
    '01100001': '', 
    '01101110': '', 
    '00100000': '', 
    '01010010': '', 
    '01101111': '', 
    '01100011': '', 
    '01101011': '', 
    '01110011': '',
    '01110111': '',
    '01000100': '',
    '01110111': '',
    '00111100': '',
    '00111110': '',
    '00111010': '',
    '01001101': '',
    '01000011': '',
    '01010011': '',

    # Symbols
    '...': '.',
    ';': '.',
    '"': '',
    '  ': ' ',
    ' - ': ', ',
    ' -,': ','
}


def get_hash(text):
    hash_object = hashlib.md5(text.encode())
    return hash_object.hexdigest()

def create_output_subdirs(subdir: str):
    output_subdir = os.path.join(SOUND_OUTPUT_FOLDER, subdir)
    if not os.path.exists(output_subdir):
        os.makedirs(output_subdir)

def prune_quest_id_table(quest_id_table):
    def is_single_quest_id(nested_dict):
        if isinstance(nested_dict, dict):
            if len(nested_dict) == 1:
                return is_single_quest_id(next(iter(nested_dict.values())))
            else:
                return False
        else:
            return True

    def single_quest_id(nested_dict):
        if isinstance(nested_dict, dict):
            return single_quest_id(next(iter(nested_dict.values())))
        else:
            return nested_dict

    pruned_table = {}
    for source_key, source_value in quest_id_table.items():
        pruned_table[source_key] = {}
        for title_key, title_value in source_value.items():
            if is_single_quest_id(title_value):
                pruned_table[source_key][title_key] = single_quest_id(title_value)
            else:
                pruned_table[source_key][title_key] = {}
                for npc_key, npc_value in title_value.items():
                    if is_single_quest_id(npc_value):
                        pruned_table[source_key][title_key][npc_key] = single_quest_id(npc_value)
                    else:
                        pruned_table[source_key][title_key][npc_key] = npc_value

    return pruned_table

def convert_ogg_to_wav(input_file, output_file=None):
    """Konvertiert eine OGG-Datei in WAV, 22050 Hz, Mono, 16-bit PCM."""
    output_file = output_file or input_file.rsplit(".", 1)[0] + ".wav"
    audio = AudioSegment.from_ogg(input_file)
    
    # Mono und 22050 Hz sicherstellen
    audio = audio.set_channels(1).set_frame_rate(22050).set_sample_width(2)  # 2 bytes = 16-bit
    
    audio.export(output_file, format="wav")
    print(f"[OGG->WAV] {input_file} -> {output_file}")

def convert_mp3_to_wav(input_file, output_file=None):
    """Konvertiert eine MP3-Datei in WAV, 22050 Hz, Mono, 16-bit PCM."""
    output_file = output_file or input_file.rsplit(".", 1)[0] + ".wav"
    audio = AudioSegment.from_mp3(input_file)
    
    # Mono und 22050 Hz sicherstellen
    audio = audio.set_channels(1).set_frame_rate(22050).set_sample_width(2)  # 2 bytes = 16-bit
    
    audio.export(output_file, format="wav")
    print(f"[MP3->WAV] {input_file} -> {output_file}")

def convert_wav_to_mp3(input_file, output_file):
    audio = AudioSegment.from_wav(input_file)
    audio.export(output_file, format="mp3", bitrate="64k")

import json
import random
from collections import defaultdict

def create_voice_clone_map():
    minAudioLength = 7.0
    maxAudioLength = 25.0
    # --- Laden ---
    with open('./sql.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    with open('./gossip.json', 'r', encoding='utf-8') as f:
        gossip = json.load(f)
    with open('./sound_length.json', 'r', encoding='utf-8') as f:
        length = json.load(f)

    print('processing data')

    # name -> {'quests': set(), 'gossip': set()}
    soundFiles = defaultdict(lambda: {'quests': set(), 'gossip': set()})

    # --- EIN Durchlauf über data ---
    for entry in data:
        name = entry['name']
        source = entry['source']

        if source in ('accept', 'complete'):
            value = f"{entry['quest']}-{source}"
            if length.get(value, 0) > minAudioLength:
                soundFiles[name]['quests'].add(value)

        elif source == 'gossip' and name in gossip:
            for value in gossip[name].values():
                if length.get(value, 0) > minAudioLength:
                    soundFiles[name]['gossip'].add(value)

    # gender-race -> set(soundpaths)
    genderRaceMap = defaultdict(set)

    for entry in data:
        name = entry['name']
        key = f"{entry['DisplayRaceID']}-{entry['DisplaySexID']}"

        for value in soundFiles[name]['quests']:
            genderRaceMap[key].add(f"quests/{value}")

        for value in soundFiles[name]['gossip']:
            genderRaceMap[key].add(f"gossip/{value}")

    # --- Voice Clone Map ---
    voiceCloneFile = {}

    for entry in data:
        name = entry['name']
        key = f"{entry['DisplayRaceID']}-{entry['DisplaySexID']}"

        if key == '10-1':
            key = '5-1'

        if name not in voiceCloneFile:
            # random.choice braucht eine Sequenz
            voiceCloneFile[name] = random.choice(tuple(genderRaceMap[key]))

    # --- Schreiben ---
    with open('voice-clone-map.json', 'w', encoding='utf-8') as f:
        json.dump(voiceCloneFile, f, ensure_ascii=False, indent=4)

    print("Gefilterte Daten erfolgreich gespeichert.")

class TTSProcessor:
    def __init__(self, tts_lang):
        self.tts_lang = tts_lang
        print('TTSProcessor initialized with language: ', self.get_tts_lang())
        
        # Lade die Daten aus der Eingabe-JSON-Datei
        with open('./voice-clone-map.json', 'r', encoding='utf-8') as infile:
            self.voiceCloneMap = json.load(infile)

    def get_tts_lang(self):
        return self.tts_lang
    
    def tts(self, name: str, text: str, outputName: str, output_subfolder: str, forceGen: bool = False):
        result = ""
        outpath = os.path.join(SOUND_OUTPUT_FOLDER, output_subfolder, outputName)
        voice_id = self.voiceCloneMap[name]

        if os.path.isfile(f"{outpath}.mp3") and forceGen is not True:
            return "duplicate generation, skipping"

        print(outputName)
        print(outpath)
        print(f"Using voice_id: {voice_id}")

        try:
            text = text.strip()
            
            # Prepare request to TTS webservice
            api_url = "http://localhost:8000/api/v1/synthesize"
            payload = {
                "text": text,
                "voice_id": voice_id,
                "language": "german",
                "temperature": 0.6,
                "top_p": 0.65,
                "top_k": 45,
                "repetition_penalty": 10.0,
                "length_penalty": 0.65,
                "gpt_cond_len": 30,
                "gpt_cond_chunk_len": 4,
                "max_ref_len": 30
            }
            
            # Send POST request to TTS service
            response = requests.post(api_url, json=payload, timeout=300)
            response.raise_for_status()
            
            # Parse response
            response_data = response.json()
            file_path = response_data.get("file_path")
            
            if not file_path:
                raise Exception("No file_path in response")
            
            # Download the generated audio file
            download_url = f"http://localhost:8000/api/v1{file_path}"
            audio_response = requests.get(download_url, timeout=60)
            audio_response.raise_for_status()
            
            # Ensure output directory exists
            os.makedirs(os.path.dirname(f"{outpath}.mp3"), exist_ok=True)
            
            # Save the audio file with the correct name
            with open(f"{outpath}.mp3", "wb") as f:
                f.write(audio_response.content)
            
            result = f"Audio file saved successfully via webservice: {outpath}.mp3"
            
        except requests.exceptions.RequestException as e:
            print(f"Error: unable to generate audio via webservice {outpath}: {e}")
            result = f"Error: unable to generate audio via webservice {outpath}: {e}"
        except Exception as e:
            print(f"Error: unable to save audio file {outpath}: {e}")
            result = f"Error: unable to save audio file {outpath}: {e}"

        return result
        
    def handle_gender_options(self, text):
        pattern = re.compile(r'\$[Gg]\s*([^:;]+?)\s*:\s*([^:;]+?)\s*;')

        male_text = pattern.sub(r'\1', text)
        female_text = pattern.sub(r'\2', text)

        return male_text, female_text

    def preprocess_dataframe(self, df):
        df = df.copy()  

        df['race'] = df['DisplayRaceID'].map(RACE_DICT)
        df['gender'] = df['DisplaySexID'].map(GENDER_DICT)
        df['voice_name'] = df['race'] + '-' + df['gender']

        df['templateText_race_gender_hash'] = self.get_race_gender_hash(
            df['original_text'], df['race'], df['gender']
        )
        rows = []

        for _, row in df.iterrows():
            variants = self._expand_text_variants(row.to_dict())

            for variant in variants:
                new_row = row.copy()
                new_row['text'] = variant['text']
                new_row['cleanedText'] = self.clean_text(variant['text'])
                new_row['player_gender'] = variant.get('player_gender')

                rows.append(new_row)

        new_df = pd.DataFrame(rows).reset_index(drop=True)

        return new_df


    def process_row(self, row):
        if "$" in row.cleanedText or "<" in row.cleanedText or ">" in row.cleanedText:
            return f'skipping due to invalid chars: {row.cleanedText}'
        else:
            return self.tts_row(row)

    def tts_row(self, row):
        tts_text = row.cleanedText
        entry = {
            "quest": getattr(row, "quest", None),
            "source": getattr(row, "source", None),
            "DisplayRaceID": row.DisplayRaceID,
            "DisplaySexID": row.DisplaySexID,
            "original_text": row.original_text,
            "player_gender": row.player_gender
        }

        subfolder, file_name = self._get_output_target(entry)
        
        if row.player_gender is not None:
            file_name = row.player_gender+ '-' + file_name

        return self.tts(row.name, tts_text, file_name, subfolder)

    def create_output_dirs(self):
        create_output_subdirs('')
        create_output_subdirs('quests')
        create_output_subdirs('gossip')

    def chunkify(self, df, chunk_size):
        for i in range(0, len(df), chunk_size):
            yield df.iloc[i:i + chunk_size]

    def process_chunk(self, df_chunk, row_processing_fn):
        last_message = None

        for row in df_chunk.itertuples(index=False):
            last_message = row_processing_fn(row)

        return len(df_chunk), last_message


    def process_rows_in_parallel(self, df, row_processing_fn, max_workers=None, chunk_size=50):
        total_rows = len(df)

        bar_format = (
            '{l_bar}{bar}| {n_fmt}/{total_fmt} '
            '[{elapsed}<{remaining}, {rate_fmt}] {postfix}'
        )

        with tqdm(
            total=total_rows,
            unit='rows',
            ncols=100,
            desc='Generating Audio',
            bar_format=bar_format,
            dynamic_ncols=True
        ) as pbar:

            with ProcessPoolExecutor(max_workers=max_workers) as executor:

                futures = [
                    executor.submit(
                        self.process_chunk,
                        chunk,
                        row_processing_fn
                    )
                    for chunk in self.chunkify(df, chunk_size)
                ]

                for future in as_completed(futures):
                    processed_rows, last_message = future.result()
                    pbar.update(processed_rows)
                    if last_message:
                        pbar.set_postfix_str(last_message)

    def process_rows_serial(self, df, row_processing_fn):
        total_rows = len(df)
        bar_format = '{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}] {postfix}'

        with tqdm(
            total=total_rows,
            unit='rows',
            ncols=100,
            desc='Generating Audio',
            ascii=False,
            bar_format=bar_format,
            dynamic_ncols=True
        ) as pbar:

            for row in df.itertuples(index=False):
                custom_message = row_processing_fn(row)
                if custom_message:
                    pbar.set_postfix_str(custom_message)
                pbar.update(1)

    def write_gossip_file_lookups_table(self, df, module_name, type, table, filename):
        output_file = OUTPUT_FOLDER + f"/{filename}.lua"
        gossip_table = {}

        accept_df = df[(df['quest'] == '') & (df['type'] == type)]

        for i, row in tqdm(accept_df.iterrows()):
            if row['id'] not in gossip_table:
                gossip_table[row['id']] = {}

            escapedText = row['text'].replace('"', '\'').replace('\r',' ').replace('\n',' ')

            gossip_table[row['id']][escapedText] = row['templateText_race_gender_hash']

        with open(output_file, "w", encoding="UTF-8") as f:
            f.write(DATAMODULE_TABLE_GUARD_CLAUSE + "\n")
            f.write(f"{module_name}.{table} = ")
            f.write(lua.encode(gossip_table))
            f.write("\n")

        print(f"Finished writing {filename}.lua")


    def write_questlog_npc_lookups_table(self, df, module_name, type, table, filename):
        output_file = OUTPUT_FOLDER + f"/{filename}.lua"
        questlog_table = {}

        accept_df = df[(df['source'] == 'accept') & (df['type'] == type)]

        for i, row in tqdm(accept_df.iterrows()):
            questlog_table[int(row['quest'])] = row['id']

        with open(output_file, "w", encoding="UTF-8") as f:
            f.write(DATAMODULE_TABLE_GUARD_CLAUSE + "\n")
            f.write(f"{module_name}.{table} = ")
            f.write(lua.encode(questlog_table))
            f.write("\n")

        print(f"Finished writing {filename}.lua")

    def write_npc_name_lookup_table(self, df, module_name, type, table, filename):
        output_file = OUTPUT_FOLDER + f"/{filename}.lua"
        npc_name_table = {}

        accept_df = df[df['type'] == type]

        for i, row in tqdm(accept_df.iterrows()):
            npc_name_table[row['id']] =  row['name']

        with open(output_file, "w", encoding="UTF-8") as f:
            f.write(DATAMODULE_TABLE_GUARD_CLAUSE + "\n")
            f.write(f"{module_name}.{table} = ")
            f.write(lua.encode(npc_name_table))
            f.write("\n")

        print(f"Finished writing {filename}.lua")

    def write_quest_id_lookup(self, df, module_name):
        output_file = OUTPUT_FOLDER + "/quest_id_lookups.lua"
        quest_id_table = {}

        quest_df = df[df['quest'] != '']

        for i, row in tqdm(quest_df.iterrows()):
            quest_source = row['source']
            if quest_source == 'progress': # skipping progress text for now
                continue

            quest_id = int(row['quest'])
            quest_title = row['quest_title']
            quest_text = get_first_n_words(row['text'], 15) + ' ' +  get_last_n_words(row['text'], 15)
            escaped_quest_text = replace_dollar_bs_with_space(quest_text.replace('"', '\'').replace('\r',' ').replace('\n',' '))
            escaped_quest_title = quest_title.replace('"', '\'').replace('\r',' ').replace('\n',' ')
            npc_name = row['name']
            escaped_npc_name = npc_name.replace('"', '\'').replace('\r',' ').replace('\n',' ')

            # table[source][title][npcName][text]
            if quest_source not in quest_id_table:
                quest_id_table[quest_source] = {}

            if escaped_quest_title not in quest_id_table[quest_source]:
                quest_id_table[quest_source][escaped_quest_title] = {}

            if escaped_npc_name not in quest_id_table[quest_source][escaped_quest_title]:
                quest_id_table[quest_source][escaped_quest_title][escaped_npc_name] = {}

            if quest_text not in quest_id_table[quest_source][escaped_quest_title][escaped_npc_name]:
                quest_id_table[quest_source][escaped_quest_title][escaped_npc_name][escaped_quest_text] = quest_id

        pruned_quest_id_table = prune_quest_id_table(quest_id_table)

        # UTF-8 Encoding is important for other languages!
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(DATAMODULE_TABLE_GUARD_CLAUSE + "\n")
            f.write(f"{module_name}.QuestIDLookup = ")
            f.write(lua.encode(pruned_quest_id_table))
            f.write("\n")

    def write_npc_name_gossip_file_lookups_table(self, df, module_name, type, table, filename):
        output_file = OUTPUT_FOLDER + f"/{filename}.lua"
        gossip_table = {}

        accept_df = df[(df['quest'] == '') & (df['type'] == type)]

        for i, row in tqdm(accept_df.iterrows()):
            npc_name = row['name']
            escaped_npc_name = npc_name.replace('"', '\'').replace('\r',' ').replace('\n',' ')

            if escaped_npc_name not in gossip_table:
                gossip_table[escaped_npc_name] = {}

            escapedText = row['text'].replace('"', '\'').replace('\r',' ').replace('\n',' ')

            gossip_table[escaped_npc_name][escapedText] = row['templateText_race_gender_hash']

        with open(output_file, "w", encoding="UTF-8") as f:
            f.write(DATAMODULE_TABLE_GUARD_CLAUSE + "\n")
            f.write(f"{module_name}.{table} = ")
            f.write(lua.encode(gossip_table))
            f.write("\n")

        print(f"Finished writing {filename}.lua")

    def tts_dataframe(self, df):
        self.create_output_dirs()
        self.process_rows_serial(df, self.process_row)
        print("Audio finished generating.")

    def generate_lookup_tables(self, df):
        self.create_output_dirs()
        self.write_gossip_file_lookups_table(df, MODULE_NAME, 'creature',   'GossipLookupByNPCID',    'npc_gossip_file_lookups')
        self.write_gossip_file_lookups_table(df, MODULE_NAME, 'gameobject', 'GossipLookupByObjectID', 'object_gossip_file_lookups')

        self.write_quest_id_lookup(df, MODULE_NAME)
        print("Finished writing quest_id_lookups.lua")

        self.write_npc_name_gossip_file_lookups_table(df, MODULE_NAME, 'creature',   'GossipLookupByNPCName',    'npc_name_gossip_file_lookups')
        self.write_npc_name_gossip_file_lookups_table(df, MODULE_NAME, 'gameobject', 'GossipLookupByObjectName', 'object_name_gossip_file_lookups')

        self.write_questlog_npc_lookups_table(df, MODULE_NAME, 'creature',   'NPCIDLookupByQuestID',    'questlog_npc_lookups')
        self.write_questlog_npc_lookups_table(df, MODULE_NAME, 'gameobject', 'ObjectIDLookupByQuestID', 'questlog_object_lookups')
        self.write_questlog_npc_lookups_table(df, MODULE_NAME, 'item',       'ItemIDLookupByQuestID',   'questlog_item_lookups')

        self.write_npc_name_lookup_table(df, MODULE_NAME, 'creature',   'NPCNameLookupByNPCID',       'npc_name_lookups')
        self.write_npc_name_lookup_table(df, MODULE_NAME, 'gameobject', 'ObjectNameLookupByObjectID', 'object_name_lookups')
        self.write_npc_name_lookup_table(df, MODULE_NAME, 'item',       'ItemNameLookupByItemID',     'item_name_lookups')

        write_sound_length_table_lua(MODULE_NAME, SOUND_OUTPUT_FOLDER, OUTPUT_FOLDER)
        print("Updated sound_length_table.lua")
    
    def _load_output_json(self):
        with open("./output.json", "r", encoding="utf-8") as f:
            return json.load(f)
    def _load_voice_clone_map_json(self):
        with open("./voice-clone-map.json", "r", encoding="utf-8") as f:
            return json.load(f)
    def _find_quest_entry(self, data, quest_source):
        # quest_source = "70-accept"
        quest_id, source = quest_source.split("-", 1)

        for entry in data:
            if (
                entry.get("quest") == quest_id and
                entry.get("source") == source
            ):
                return entry
        return None
    
    def _find_gossip_entry(self, data, search_hash):
        for entry in data:
            if entry.get("quest"):
                continue

            hash = self.get_race_gender_hash(entry["original_text"], RACE_DICT.get(entry["DisplayRaceID"], ""), GENDER_DICT.get(entry["DisplaySexID"], ""))

            if hash == search_hash:
                return entry

        return None

    def _regenerate_from_entry(self, entry):
        name = entry["name"]

        cleaned_text = self.clean_text(entry["text"])

        subfolder, file_name = self._get_output_target(entry)
        
        return self.tts(
            name=name,
            text=cleaned_text,
            outputName=file_name,
            output_subfolder=subfolder,
            forceGen=True
        )

    def regenerate_audio(self, kind: str, identifier: str, language_number: int):
        data = self._load_output_json()

        if kind == "quest":
            entry = self._find_quest_entry(data, identifier)
            
            if not entry:
                print(f"No quest entry found for {identifier}")
                return
            
            variants = self._expand_text_variants(entry)

            for variant in variants:
                result = self._regenerate_from_entry(variant)
        
                print(result)

        elif kind == "gossip":
            entry = self._find_gossip_entry(data, identifier)
            if not entry:
                print(f"No gossip entry found for hash {identifier}")
                return

            variants = self._expand_text_variants(entry)

            for variant in variants:
                result = self._regenerate_from_entry(variant)
        
                print(result)

    def regenerate_for_npc(self, npc_name: str):
        data = self._load_output_json()

        entries = [e for e in data if e.get("name") == npc_name]
        matches = []

        for entry in entries:
            variants_for_entry = self._expand_text_variants(entry)

            for variant in variants_for_entry:
                matches.append(variant)

        if not matches:
            print(f"No entries found for NPC '{npc_name}'")
            return

        print(f"Found {len(matches)} entries for NPC '{npc_name}'")

        self.regenerate_entries_with_progress(matches)

    def _load_voice_clone_map(self):
        with open("./voice-clone-map.json", "r", encoding="utf-8") as f:
            return json.load(f)

    def _save_voice_clone_map(self, data):
        with open("./voice-clone-map.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def switch_voice(self, old_voice: str, new_voice: str):
        voice_map = self._load_voice_clone_map()

        affected_npcs = []

        for npc_name, voice in voice_map.items():
            if voice == old_voice:
                voice_map[npc_name] = new_voice
                affected_npcs.append(npc_name)

        if not affected_npcs:
            print(f"No NPCs found using voice '{old_voice}'")
            return

        self._save_voice_clone_map(voice_map)

        print(
            f"Replaced voice '{old_voice}' with '{new_voice}' "
            f"for {len(affected_npcs)} NPC(s)"
        )

        # 🔥 Wichtig: internen Cache aktualisieren
        self.voiceCloneMap = voice_map

        current_npc = 1
        # 🎙 Regenerate Audio
        for npc_name in affected_npcs:
            print(f"\n{current_npc}/{len(affected_npcs)} Regenerating audio for NPC: {npc_name}")
            current_npc += 1
            self.regenerate_for_npc(npc_name)

    def get_race_gender_hash(self, original_text, race, gender):
        """
        Funktioniert mit:
        - Strings
        - pandas.Series
        Liefert exakt denselben Hash wie die ursprüngliche DF-Implementierung.
        """

        if isinstance(original_text, pd.Series):
            template = original_text + race + gender
            return template.apply(get_hash)

        if race is None or gender is None:
            return None

        return get_hash(original_text + race + gender)

    def clean_text(self, text):
        """
        Bereinigt Text entweder als String oder als pandas.Series.
        """
        is_series = isinstance(text, pd.Series)

        result = text.copy() if is_series else text

        for k, v in REPLACE_DICT.items():
            if is_series:
                result = result.str.replace(k, v, regex=False)
            else:
                result = result.replace(k, v)

        if is_series:
            result = result.str.replace(r'<.*?>\s', '', regex=True)
        else:
            import re
            result = re.sub(r'<.*?>\s', '', result)

        return result
    
    def _get_output_target(self, entry):
        """
        Ermittelt Subfolder und Basis-Dateinamen (ohne Gender-Suffix).
        """
        if entry.get("quest"):
            file_name = f'{entry["quest"]}-{entry["source"]}'
            subfolder = "quests"
        else:
            race = RACE_DICT.get(entry["DisplayRaceID"], "")
            gender = GENDER_DICT.get(entry["DisplaySexID"], "")
            file_name = self.get_race_gender_hash(
                entry["original_text"], race, gender
            )
            subfolder = "gossip"


        if entry['player_gender'] is not None:
            file_name = entry['player_gender'] + '-' + file_name

        return subfolder, file_name

    def _expand_text_variants(self, entry):
        """
        Erzeugt Textvarianten anhand erkannter Platzhalter.
        Rückgabe: Liste von Dicts mit Metadaten.
        """

        variants = []

        # --------------------------------------------------
        # GENDER ($G / $g)
        # --------------------------------------------------
        if re.search(r'\$[Gg]', entry['text']):
            male_text, female_text = self.handle_gender_options(entry['text'])
            variants.append({
                **entry,
                "text": male_text,
                "player_gender": "m",
            })
            variants.append({
                **entry,
                "text": female_text,
                "player_gender": "f",
            })

            return variants  # bewusst: Gender ist exklusiv

        # --------------------------------------------------
        # DEFAULT (keine Varianten)
        # --------------------------------------------------
        variants.append({
            **entry,
            "text": entry['text'],
            "player_gender": None,
        })

        return variants
    
    def regenerate_by_text(self, search: str):
        data = self._load_output_json()

        search_lower = search.lower()
        matches = []

        for entry in data:
            text = entry["text"]
            if search_lower in text.lower():
                variants_for_entry = self._expand_text_variants(entry)

                for variant in variants_for_entry:
                    matches.append(variant)

        if not matches:
            print(f"No entries found containing '{search}'")
            return

        print(f"Found {len(matches)} entries containing '{search}'")

        self.regenerate_entries_with_progress(matches)

    def regenerate_by_race(self, race_id: int, sex_id: int | None = None):
        data = self._load_output_json()

        matches = []

        for entry in data:
            if entry.get("DisplayRaceID") != race_id:
                continue

            if sex_id is not None and entry.get("DisplaySexID") != sex_id:
                continue

            variants_for_entry = self._expand_text_variants(entry)

            for variant in variants_for_entry:
                matches.append(variant)
            

        if not matches:
            if sex_id is None:
                print(f"No entries found for DisplayRaceID {race_id}")
            else:
                print(
                    f"No entries found for DisplayRaceID {race_id} "
                    f"and DisplaySexID {sex_id}"
                )
            return

        if sex_id is None:
            print(f"Found {len(matches)} entries for DisplayRaceID {race_id}")
        else:
            print(
                f"Found {len(matches)} entries for DisplayRaceID {race_id} "
                f"and DisplaySexID {sex_id}"
            )

        self.regenerate_entries_with_progress(matches)

    def regenerate_entries_with_progress(self, entries, desc="Regenerating Audio"):
        total = len(entries)
        bar_format = '{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}] {postfix}'

        with tqdm(
            total=total,
            unit='files',
            ncols=100,
            desc=desc,
            ascii=False,
            bar_format=bar_format,
            dynamic_ncols=True
        ) as pbar:

            for entry in entries:
                postfix = self._regenerate_from_entry(entry)
                if postfix:
                    pbar.set_postfix_str(postfix)
                pbar.update(1)

    def regenerate_all_with_voice(self, voice: str):
        voice_map = self._load_voice_clone_map_json()

        matching_npcs = [
            npc_name
            for npc_name, npc_voice in voice_map.items()
            if npc_voice == voice
        ]

        if not matching_npcs:
            print(f"No NPCs found with voice '{voice}'")
            return

        print(f"Found {len(matching_npcs)} NPC(s) with voice '{voice}'")

        current_npc = 1;

        for npc_name in matching_npcs:
            print(f"{current_npc}/{len(matching_npcs)} Regenerating audio for NPC: {npc_name}")
            current_npc += 1;
            self.regenerate_for_npc(npc_name)
