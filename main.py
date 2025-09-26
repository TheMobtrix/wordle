from game import WordleGame

def main():
    """
    The main entry point for the Wordle game application.
    """
    print("==============================")
    print("   Welcome to Python Wordle   ")
    print("==============================")
    print("Guess the 5-letter word in 6 tries.")

    word_file = "words_generated.txt"

    game = WordleGame(word_file)
    game.play()

    print("\nThanks for playing!")

if __name__ == "__main__":
    main()
