import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt')  
nltk.download('stopwords')  

# Read reviews from a file
reviews = []
with open('./output/DecodedEmoji.txt', 'r', encoding='utf-8') as file:
    for review in file:
        reviews.append(review.strip())  # Remove extra spaces and newlines

# Preprocessing function
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove digits
    text = re.sub(r'\d+', '', text)
    # Remove special characters
    text = re.sub(r'[^\w\s]', '', text)
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    # Tokenize
    tokens = word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    # Join tokens back into a single string
    return ' '.join(tokens)

# Preprocess all reviews
preprocessed_reviews = [preprocess_text(review) for review in reviews]

# Create a DataFrame
df = pd.DataFrame(preprocessed_reviews, columns=['review'])

# Save preprocessed reviews to a CSV file
df.to_csv('./PreprocessedReviews.csv', index=False)
