import googletrans as gt

def confidence(word, translator):
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

        filtered_data = []
        emt_str = words[0]

        for i in range(1, len(words)):
            if confidence(words[i], translator) == confidence(words[i-1], translator):
                emt_str += ' ' + words[i]
            else:
                if emt_str:
                    filtered_data.append(emt_str)
                emt_str = words[i]
        if emt_str:
            filtered_data.append(emt_str)

        for word in filtered_data:
            language = confidence(word, translator)
            if language == 'te':
                new_word = translate_text(word, translator, 'te')
                translated_line.append(new_word)
            elif language == 'hi':
                new_word = translate_text(word, translator, 'hi')
                translated_line.append(new_word)
            else:
                translated_line.append(word)
        output_txt.write(' '.join(translated_line) + '\n')
