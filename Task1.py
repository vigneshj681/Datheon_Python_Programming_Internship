#!/usr/bin/env python3
"""Terminal Hangman: guess the hidden word letter by letter within 6 mistakes."""

import random

MAX_MISTAKES = 6

WORDS = [
    "python", "variable", "function", "keyboard", "algorithm", "database",
    "network", "compiler", "terminal", "software", "hardware", "internet",
    "programming", "developer", "debugging", "framework", "interface",
    "elephant", "mountain", "chocolate", "adventure", "umbrella", "hospital",
    "universe", "telephone", "butterfly", "calendar", "language", "notebook",
]

# One ASCII picture per number of mistakes (0 through 6).
STAGES = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """,
]


def mask_word(word, correct):
    """Return the word with unguessed letters shown as underscores."""
    return " ".join(ch.upper() if ch in correct else "_" for ch in word)


def display(word, correct, wrong):
    """Print the current game state."""
    print(STAGES[len(wrong)])
    print("Word:   ", mask_word(word, correct))
    print("Wrong:  ", " ".join(sorted(l.upper() for l in wrong)) or "-")
    print(f"Lives:   {MAX_MISTAKES - len(wrong)}/{MAX_MISTAKES}\n")


def get_guess(guessed):
    """Prompt until the player enters a single new letter."""
    while True:
        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (A-Z).")
        elif guess in guessed:
            print(f"You already guessed '{guess.upper()}'. No penalty - try another.")
        else:
            return guess


def play_round():
    """Play one game. Returns True if the player won."""
    word = random.choice(WORDS)
    correct = set()   # correctly guessed letters
    wrong = set()     # incorrectly guessed letters
    letters_needed = set(word)

    print("\n=== HANGMAN ===")
    print(f"The word has {len(word)} letters. You may miss {MAX_MISTAKES} times.")

    while len(wrong) < MAX_MISTAKES and not letters_needed <= correct:
        display(word, correct, wrong)
        guess = get_guess(correct | wrong)

        if guess in word:
            correct.add(guess)
            print(f"Good guess! '{guess.upper()}' is in the word.")
        else:
            wrong.add(guess)
            print(f"Sorry, '{guess.upper()}' is not in the word.")

    display(word, correct, wrong)
    if letters_needed <= correct:
        print(f"You won! The word was '{word.upper()}'.")
        return True
    print(f"You lost! The word was '{word.upper()}'.")
    return False


def main():
    wins = losses = 0
    while True:
        if play_round():
            wins += 1
        else:
            losses += 1
        print(f"\nScore - Wins: {wins}  Losses: {losses}")
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
