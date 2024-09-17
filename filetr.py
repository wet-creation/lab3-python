import os
import json
import re
from lab3 import google_trans as gt


def analyze_text(text):
    sentences = re.split(r'[.!?]+', text)
    words = text.split()
    characters = len(text)
    return characters, len(words), len(sentences)


def load_config(config_path):
    try:
        with open(config_path, 'r') as file:
            config = json.load(file)
        return config
    except Exception as e:
        raise Exception(f"Error loading configuration file: {e}")




def main():
    config_file = 'config.json'

    try:
        config = load_config(config_file)
        text_file = config["text_file"]
        target_language = config["target_language"]
        output = config["output"]
        max_chars = config["max_chars"]
        max_words = config["max_words"]
        max_sentences = config["max_sentences"]

        if not os.path.exists(text_file):
            raise FileNotFoundError(f"Text file '{text_file}' not found!")

        with open(text_file, 'r', encoding='utf-8') as file:
            text = file.read()

        chars, words, sentences = analyze_text(text)

        print(f"File: {text_file}")
        print(f"Size: {os.path.getsize(text_file)} bytes")
        print(f"Characters: {chars}")
        print(f"Words: {words}")
        print(f"Sentences: {sentences}")

        if chars > max_chars or words > max_words or sentences > max_sentences:
            text = text[:max_chars]

        detected_lang = gt.LangDetect(text)
        print(f"Detected language: {detected_lang}")

        translated_text = gt.TransLate(text, target_language.lower())

        if output == "screen":
            print(f"Translation to {target_language}:\n{translated_text}")
        elif output == "file":
            output_file = f"{os.path.splitext(text_file)[0]}_{target_language}.txt"
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(translated_text)
            print("Ok")
        else:
            raise ValueError("Invalid output option specified in config file.")

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
