from collections import Counter
import re

# Read text file
with open("sample_text.txt", "r") as file:
    text = file.read().lower()

# Remove punctuation
text = re.sub(r'[^\w\s]', '', text)

words = text.split()

# Count word frequency
word_counts = Counter(words)

# Print results
for word, count in word_counts.items():
    print(f"{word}: {count}")
