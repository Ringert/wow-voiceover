import argparse
from tts_cli.sql_queries import query_dataframe_for_all_quests_and_gossip, fix_german_for_tts
from tts_cli.tts_cloning import TTSProcessor, create_voice_clone_map
from tts_cli.init_db import download_and_extract_latest_db_dump, import_sql_files_to_database
from tts_cli.wrath_model_extraction import write_model_data
from tts_cli import utils
import warnings

warnings.filterwarnings("ignore")

parser = argparse.ArgumentParser(
    description="Text-to-Speech CLI for WoW dialog")
    
parser.add_argument("--lang", default="deDE")

subparsers = parser.add_subparsers(dest="mode", help="Available modes")
subparsers.add_parser("init-db", help="Initialize the database")
subparsers.add_parser("fix-de", help="Fix german text for TTS")
subparsers.add_parser("interactive", help="Interactive mode")
subparsers.add_parser("extract_model_data", help="Generate info about which NPC entry uses which model.")
subparsers.add_parser("create_voice_clone_map", help="Generate info about which NPC entry uses which model.")
subparsers.add_parser("gen_lookup_tables", help="Generate the lookup tables for all quests and gossip in the game. Also recomputes the sound length table.").add_argument("--lang", default="enUS")

args = parser.parse_args()

language_code = args.lang
language_number = utils.language_code_to_language_number(language_code)
print(f"Selected language: {language_code}")

def interactive_mode():
    tts_processor = TTSProcessor(utils.language_number_to_tts_lang(language_number))
    df = query_dataframe_for_all_quests_and_gossip(language_number)
    df = tts_processor.preprocess_dataframe(df)
    tts_processor.tts_dataframe(df)

if args.mode == "init-db":
    download_and_extract_latest_db_dump()
    import_sql_files_to_database()
    fix_german_for_tts()
    print("Database initialized successfully.")
elif args.mode == "fix-de":
    fix_german_for_tts()
elif args.mode == "interactive":
    interactive_mode()
elif args.mode == "gen_lookup_tables":
    tts_processor = TTSProcessor(utils.language_number_to_tts_lang(language_number))

    df = query_dataframe_for_all_quests_and_gossip(language_number)
    df = tts_processor.preprocess_dataframe(df)
    tts_processor.generate_lookup_tables(df)
elif args.mode == "extract_model_data":
    write_model_data()
elif args.mode == "create_voice_clone_map":
    create_voice_clone_map();
else:
    interactive_mode()

