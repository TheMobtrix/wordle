import random

class WordBank:
    def __init__(self, words):
        self._load_words(word_file_path)
    
    def _load_words(self, word_file_path):
        try:
            with open(word_file_path, 'r') as f:
                 return [word.strip().upper() for word in f if word.strip()]
        except FileNotFoundError:
            print(f"Error: Word file not found at '{file_path}'.")
            return []


    def get_random_word(self):
        if not self.words:
            raise ValueError("Word list is empty.")
        return random.choice(self.words)