import json

def load_emoji_mappings(filename):
    with open(filename, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)

def replace_emojis(review, emoji_to_text):
    for emoji, meaning in emoji_to_text.items():
        review = review.replace(emoji, meaning)
    return review

# Load the JSON file
emoji_to_text = load_emoji_mappings('emoji_to_text.json')

# Read input file and process each line
with open('input.txt', 'r', encoding='utf-8') as input_file, open('output.txt', 'w', encoding='utf-8') as output_file:
    for review in input_file:
        processed_review = replace_emojis(review, emoji_to_text)
        output_file.write(processed_review)
