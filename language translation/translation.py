import googletrans as gt

def confidance(word, translator):
    detection = translator.detect(word)
    return detection.lang
    
def translate_text(text, translator, src_lang, dest_lang='en'):
    translation = translator.translate(text, src=src_lang, dest=dest_lang)
    return translation.text

with open('input.txt', 'r', encoding='utf-8') as input_file, open('output.txt', 'w', encoding='utf-8') as output_txt:
    translator = gt.Translator()
    for line in input_file:
        words = line.split()
        translated_line = []
        for word in words:
            language = confidance(word, translator)

            if language == 'te':
                new_word = translate_text(word, translator, 'te')
                translated_line.append(new_word)
            elif language == 'hi':
                new_word = translate_text(word, translator, 'hi')
                translated_line.append(new_word)
            else:
                translated_line.append(word)
        output_txt.write(' '.join(translated_line) + '\n')
