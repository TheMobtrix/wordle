import nltk
nltk.download('words')
from nltk.corpus import words

five_letter_words = sorted(list(set(
    [word.upper() for word in words.words() if len(word) == 5]
)))

# Write the words to a file
with open('words_generated.txt', 'w') as f:
    for word in five_letter_words:
        f.write(f"{word}\n")

print(f"Generated a file with {len(five_letter_words)} words.")