import re
from collections import Counter

# Predefined stop words
stop_words = set(["is", "a", "the", "for", "and", "this", "has", "with", "not", 'are', 'too'])

# Function to preprocess text
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    tokens = text.split()
    tokens = [word for word in tokens if word not in stop_words]
    return tokens

# Characteristics with related keywords
characteristics = {
    'screen': ['oled', 'lcd', 'touchscreen', 'resolution', 'crystal clear', 'dull', 'not responsive'],
    'battery': ['mah', 'long-lasting', 'fast-charging', 'drains fast', 'excellent battery life', 'short battery life'],
    'camera': ['megapixel', 'zoom', 'wide-angle', 'clarity', 'night photos', 'focus', 'flash', 'photo quality', 'features', 'blurry'],
    'performance': ['speed', 'responsive', 'sluggish', 'exceeded expectations', 'slow'],
    'price': ['affordable', 'expensive', 'worth the price', 'value for money'],
    'software': ['buggy', 'slow updates', 'features', 'updates'],
    'network': ['network issues'],
    'storage': ['storage', 'insufficient storage'],
    'charging': ['fast charging', 'slow charging'],
}

with open('emoji_to_text.txt', 'r') as input_file, open('BOW_algo_output.txt', 'w') as output_file:
    preprocessed_data = []

    for review in input_file:
        preprocessed_data.append(preprocess_text(review))

    vocabulary = set()

    for review in preprocessed_data:
        vocabulary.update(review)
    
    vocabulary = sorted(vocabulary)

    bow_vectors = []    

    for review in preprocessed_data:
        counter = Counter(review)
        bow_vector = [counter[word] for word in vocabulary]
        bow_vectors.append(bow_vector)

    characteristic_counts = {key: 0 for key in characteristics}

    for char, keywords in characteristics.items():
        for keyword in keywords:
            if keyword in vocabulary:
                index = vocabulary.index(keyword)
                for bow_vector in bow_vectors:
                    characteristic_counts[char] += bow_vector[index]

    num_reviews = len(preprocessed_data)
    characteristic_averages = {key: value / num_reviews for key, value in characteristic_counts.items()}

    output_file.write('Vocabulary => \n')
    for word in vocabulary:
        output_file.write(word + ' ')
    
    output_file.write('\n\nVector Values =>\n')
    for vector in bow_vectors:
        output_file.write(' '.join(map(str, vector)) + '\n')

    output_file.write('\n\nCharacteristic averages => \n')
    for key, value in characteristic_averages.items():
        output_file.write(f'{key}: {value}\n')


    print("Vocabulary:", vocabulary)
    print("BoW Vectors:", bow_vectors)
    print("Characteristic Averages:", characteristic_averages)