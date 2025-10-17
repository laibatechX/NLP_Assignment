import re
import nltk
from nltk.tokenize import word_tokenize

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

# Step 1: Original tweet
tweet = "RT @JohnDoe: Loving the new AI model! 😍🔥 Check it out: https://t.co/xyz123 #AI #NLP"

print("Original:", tweet)

# Step 2: Convert to lowercase
tweet = tweet.lower()

# Step 3: Remove mentions (@username)
tweet = re.sub(r'@\w+', '', tweet)

# Step 4: Remove URLs
tweet = re.sub(r'http\S+|www\S+', '', tweet)

# Step 5: Remove hashtags (#AI -> AI)
tweet = re.sub(r'#', '', tweet)

# Step 6: Remove special characters, emojis, punctuation (keep letters and spaces)
tweet = re.sub(r'[^a-z\s]', '', tweet)

# Step 7: Remove extra spaces
tweet = re.sub(r'\s+', ' ', tweet).strip()

# Step 8: Tokenize the cleaned tweet
tokens = word_tokenize(tweet)

print("Clean Tweet:", tweet)
print("Tokens:", tokens)
