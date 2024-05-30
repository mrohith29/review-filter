import emoji

def demojise(review):
    return (emoji.demojize(review, language='alias'))

with open('input.txt', 'r', encoding='utf-8') as input_file, open('output.txt', 'w') as output_file:
    for review in input_file:
        decoded = demojise(review)
        output_file.write(decoded)