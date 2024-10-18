import argparse
import textwrap

# Deine split_sentence Funktion
def split_sentence(text, lang, text_split_length=250):
    """Preprocess the input text and group sentences without exceeding the text_split_length"""
    text_splits = []
    if text_split_length is not None and len(text) >= text_split_length:
        text_splits.append("")  # Start with an empty string for the first split
        nlp = get_spacy_lang(lang)
        nlp.add_pipe("sentencizer")
        doc = nlp(text)

        current_group = ""  # To hold the current group of sentences

        for sentence in doc.sents:
            sentence_str = str(sentence).strip()  # Remove leading/trailing spaces

            # Check if adding the current sentence exceeds the text_split_length
            if len(current_group) + len(sentence_str) + 1 <= text_split_length:
                # Add to the current group if it doesn't exceed the limit
                if current_group:
                    current_group += " "  # Add a space between sentences
                current_group += sentence_str
            else:
                # Save the current group and start a new one
                text_splits.append(current_group)
                current_group = sentence_str  # Start with the new sentence

        # Append the last group if not empty
        if current_group:
            text_splits.append(current_group)

        # Remove the initial empty string if it's there
        if len(text_splits) > 1 and text_splits[0] == "":
            del text_splits[0]

    else:
        # If text is smaller than the split length, just return the text as is
        text_splits = [text.strip()]

    return text_splits

# Die Funktion zum Laden des Sprachmodells (Dummy-Funktion zum Ersetzen)
def get_spacy_lang(lang):
    # Hier sollte der Code zum Laden des Spacy-Sprachmodells basierend auf der Sprache stehen
    import spacy
    if lang == 'de':
        return spacy.blank('de')
    elif lang == 'en':
        return spacy.blank('en')
    else:
        raise ValueError("Unsupported language")

# Argument Parsing
def main():
    parser = argparse.ArgumentParser(description="Split text into groups of sentences.")
    parser.add_argument('--text', type=str, required=True, help='The input text to split')
    parser.add_argument('--lang', type=str, default='en', help='Language of the text (default: en)')
    parser.add_argument('--length', type=int, default=250, help='Maximum split length (default: 250)')

    args = parser.parse_args()

    # Den Text splitten
    splits = split_sentence(args.text, args.lang, args.length)

    # Ausgabe der Splits
    for i, split in enumerate(splits):
        print(f"Split {i+1}: {split}")

if __name__ == "__main__":
    main()
