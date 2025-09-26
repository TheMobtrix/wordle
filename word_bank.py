import random

class WordBank:
    def __init__(self, word_file_path: str):
        self.words = self._load_words(word_file_path)

    def _load_words(self, file_path: str) -> list[str]:
        word_list = []
        try:
            with open(file_path, 'r') as f:
                for line in f:
                    word_list.append(line.strip().upper())
            if not word_list:
                raise ValueError("Word file is empty.")
            return word_list
        except FileNotFoundError:
            print(f"Error: The word file was not found at {file_path}")
            return ["ERROR"]

    def get_random_word(self) -> str:
        return random.choice(self.words)

