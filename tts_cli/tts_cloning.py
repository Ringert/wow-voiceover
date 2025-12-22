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
import torch
from TTS.api import TTS
from pydub import AudioSegment
import json
import random
from concurrent.futures import ProcessPoolExecutor, as_completed
from tqdm import tqdm
import math
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import Xtts

# TODO: make module name a cli arg when we do other expansions
MODULE_NAME = 'AI_VoiceOverData_Vanilla'
OUTPUT_FOLDER = MODULE_NAME + '/generated'
SOUND_OUTPUT_FOLDER =  OUTPUT_FOLDER + '/sounds'
SOUND_INPUT_FOLDER = OUTPUT_FOLDER + '/input-sounds'
DATAMODULE_TABLE_GUARD_CLAUSE = 'if not VoiceOver or not VoiceOver.DataModules then return end'
REPLACE_DICT = {'$B $B': '', '$b': '\n', '$B': '\n', '$n': 'Abenteurer', '$N': 'Abenteurer',
                '$C': 'Champion', '$c': 'Champion', '$R': 'Reisender', '$r': 'Reisender', 'ß': 'ss',
                'Stormwind': 'Sturmwind', 'Thunder Bluff': 'Donnerfels', 'Thunderbluff': 'Donnerfels', 
                'Undercity': 'Unterstadt', 'Ironforge': 'Eisenschmiede', 'Alteractal': 'Alteraktal', 'Lordaeron': 'Lorderon', 'Bronzebeard': 'Bronzebart', 'Ragefireabgrund': 'Flammenschlund'}

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

def convert_mp3_to_wav(input_file, output_file):
    audio = AudioSegment.from_mp3(input_file)
    audio.export(output_file, format="wav")

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
        outpath = os.path.join(SOUND_OUTPUT_FOLDER, output_subfolder, outputName + '.wav')
        outconvpath = os.path.join(SOUND_OUTPUT_FOLDER, output_subfolder, outputName + '.mp3')
        inpath = os.path.join(SOUND_INPUT_FOLDER, self.voiceCloneMap[name] + '.mp3')
        inconvpath = os.path.join(SOUND_INPUT_FOLDER, self.voiceCloneMap[name] + '.wav')

        if os.path.isfile(outconvpath) and forceGen is not True:
            return "duplicate generation, skipping"
        
        if os.path.isfile(inpath) is not True:
            return f"can't find input file for voice cloning, skipping: {inpath}"
        
        if os.path.isfile(inconvpath) is not True:
            convert_mp3_to_wav(inpath, inconvpath)

        try:
            text = text.strip()
            # Init TTS
            # Most likely downloaded to ~/.local/share/tts/tts_models--multilingual--multi-dataset--xtts_v2 -> to improve model output for certain languages edit the config.json file. 
            # This works only with my custom TTS Projekt - otherwise the model will be redownloaded
            # may use the tts_cli/model_config/xttsv2.json instead of given config.json (its improved for german language output)
            # TODO: Add new parameter to TTS initialization to pass custom config.
            tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)

            short_text = len(text) < 250
            xtreme_short_text = len(text) < 80

            # Text to speech to a file
            tts.tts_to_file(text=text, speaker_wav=inconvpath, language=self.get_tts_lang(), speed=1.12, file_path=outpath, split_sentences=not short_text)

            convert_wav_to_mp3(outpath, outconvpath)
            os.remove(outpath)

            result = f"Audio file with tts xtts_v2 lang {self.get_tts_lang()} saved successfully!: {outpath}"
        except Exception as e:
            result = f"Error: unable to save audio file {outpath}: {e}"
            
        print(result)

        return result
        
    def handle_gender_options(self, text):
        pattern = re.compile(r'\$[Gg]\s*([^:;]+?)\s*:\s*([^:;]+?)\s*;')

        male_text = pattern.sub(r'\1', text)
        female_text = pattern.sub(r'\2', text)

        return male_text, female_text

    def preprocess_dataframe(self, df):
        df = df.copy() # prevent mutation on original df for safety
        df['race'] = df['DisplayRaceID'].map(RACE_DICT)
        df['gender'] = df['DisplaySexID'].map(GENDER_DICT)
        df['voice_name'] = df['race'] + '-' + df['gender']

        df['templateText_race_gender'] = df['original_text'] + df['race'] + df['gender']
        df['templateText_race_gender_hash'] = df['templateText_race_gender'].apply(get_hash)

        df['cleanedText'] = df['text'].copy()

        for k, v in REPLACE_DICT.items():
            df['cleanedText'] = df['cleanedText'].str.replace(k, v, regex=False)

        df['cleanedText'] = df['cleanedText'].str.replace(r'<.*?>\s', '', regex=True)

        df['player_gender'] = None
        rows = []
        for _, row in df.iterrows():
            if re.search(r'\$[Gg]', row['cleanedText']):
                male_text, female_text = self.handle_gender_options(row['cleanedText'])

                row_male = row.copy()
                row_male['cleanedText'] = male_text
                row_male['player_gender'] = 'm'

                row_female = row.copy()
                row_female['cleanedText'] = female_text
                row_female['player_gender'] = 'f'

                rows.extend([row_male, row_female])
            else:
                rows.append(row)

        new_df = pd.DataFrame(rows)
        new_df.reset_index(drop=True, inplace=True)

        return new_df


    def process_row(self, row):
        if "$" in row.cleanedText or "<" in row.cleanedText or ">" in row.cleanedText:
            return f'skipping due to invalid chars: {row.cleanedText}'
        elif row.source == "progress": # skip progress text (progress text is usually better left unread since its always played before quest completion)
            return f'skipping progress text: {row.quest}-{row.source}'
        else:
            return self.tts_row(row)

    def tts_row(self, row):
        tts_text = row.cleanedText
        file_name =  f'{row.quest}-{row.source}' if row.quest else f'{row.templateText_race_gender_hash}'
        if row.player_gender is not None:
            file_name = row.player_gender+ '-'+ file_name
        file_name = file_name
        subfolder = 'quests' if row.quest else 'gossip'
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
