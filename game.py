from collections import Counter
from word_bank import WordBank

class WordleGame:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    GRAY = '\033[90m'
    RESET = '\033[0m'

    def __init__(self, word_file_path="words_generated.txt", max_guesses: int =6):
        self.word_bank = WordBank(word_file_path)
        self.secret_word = self.word_bank.get_random_word()
        self.max_guesses = max_guesses
        self.guesses_left = max_guesses
        self.guesses = []
        self.is_won = False
        self.is_lost = False

    def _get_user_guess(self) -> str:
        while True:
            guess = input("Enter your guess: ").strip().upper()
            if len(guess) != 5:
                print("Invalid guess. Please enter a 5-letter word.")
            elif not guess.isalpha():
                print("Invalid guess. Please use only letters.")
            else:
                return guess

    def _process_guess(self, guess: str):
        feedback = [''] * 5
        secret_word_counts = Counter(self.secret_word)

        for i, letter in enumerate(guess):
            if letter == self.secret_word[i]:
                feedback[i] = 'GREEN'
                secret_word_counts[letter] -= 1

        for i, letter in enumerate(guess):
            if feedback[i] == '': # Not already marked as GREEN
                if secret_word_counts[letter] > 0:
                    feedback[i] = 'YELLOW'
                    secret_word_counts[letter] -= 1
                else:
                    feedback[i] = 'GRAY'
        
        self.guesses.append((guess, feedback))
        self.guesses_left -= 1
        if guess == self.secret_word:
            self.is_won = True
            
    def _display_board(self):

        print("\n" + "="*20)
        for guess, feedback in self.guesses:
            colored_guess = ""
            for i, letter in enumerate(guess):
                if feedback[i] == 'GREEN':
                    colored_guess += f"{self.GREEN}{letter}{self.RESET} "
                elif feedback[i] == 'YELLOW':
                    colored_guess += f"{self.YELLOW}{letter}{self.RESET} "
                else:
                    colored_guess += f"{self.GRAY}{letter}{self.RESET} "
            print(colored_guess.strip())

        for _ in range(self.guesses_left):
            print("_ _ _ _ _")
        print(f"Guesses remaining: {self.guesses_left}")
        print("="*20 + "\n")

    def play(self):

        while self.guesses_left > 0 and not self.is_won:
            self._display_board()
            user_guess = self._get_user_guess()
            self._process_guess(user_guess)

        self._display_board()
        if self.is_won:
            print(f"{self.GREEN}Congratulations! You guessed the word: {self.secret_word}{self.RESET}")
        else:
            print(f"Sorry, you ran out of guesses. The word was: {self.secret_word}")

