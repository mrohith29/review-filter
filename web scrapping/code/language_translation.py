from translate import Translator
from langdetect import detect, LangDetectException

def confidence(text):
    try:
        if len(text.strip()) > 1:  # Ensure the text is not empty and has more than one character
            return detect(text)
        else:
            return 'unknown'
    except LangDetectException:
        return 'unknown'

def translate_text(text, src_lang, dest_lang='en'):
    translator = Translator(to_lang=dest_lang, from_lang=src_lang)
    translation = translator.translate(text)
    return translation

with open('../reviews.txt', 'r', encoding='utf-8') as input_file, open('../output/translated.txt', 'w', encoding='utf-8') as output_txt:
    for line in input_file:
        if not line.strip():  # Skip empty lines
            continue

        language = confidence(line)
        if language != 'en' and language != 'unknown':
            translated_line = translate_text(line, language)
        else:
            translated_line = line

        output_txt.write(translated_line)