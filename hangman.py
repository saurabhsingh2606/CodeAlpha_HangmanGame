# ============================================================
#  TASK 1 — Hangman Game
#  CodeAlpha Python Programming Internship
# ============================================================

import random

# ── 5 Predefined Words ──────────────────────────────────────
WORDS = ["python", "developer", "hangman", "keyboard", "algorithm"]

# ── ASCII Art for Hangman Stages (0 = safe, 6 = game over) ──
HANGMAN_STAGES = [
    """
       ------
       |    |
       |
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    """
]


def display_board(wrong_guesses, guessed_letters, word):
    """Print current game state."""
    print(HANGMAN_STAGES[wrong_guesses])
    print(f"  Wrong guesses left : {6 - wrong_guesses}")
    print(f"  Letters guessed    : {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}\n")

    # Show word with blanks
    display_word = " ".join(
        letter if letter in guessed_letters else "_"
        for letter in word
    )
    print(f"  Word: {display_word}\n")


def get_guess(guessed_letters):
    """Prompt the player for a valid, new single letter."""
    while True:
        guess = input("  Guess a letter: ").strip().lower()
        if len(guess) != 1:
            print("  ⚠  Please enter exactly ONE letter.")
        elif not guess.isalpha():
            print("  ⚠  Only alphabetic letters are allowed.")
        elif guess in guessed_letters:
            print(f"  ⚠  You already guessed '{guess}'. Try a different one.")
        else:
            return guess


def check_win(word, guessed_letters):
    """Return True if every letter in the word has been guessed."""
    return all(letter in guessed_letters for letter in word)


def play_game():
    """Run one full round of Hangman."""
    word           = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses  = 0
    max_wrong      = 6

    print("\n" + "=" * 45)
    print("         🎮  WELCOME TO HANGMAN!  🎮")
    print("=" * 45)
    print(f"  A random word has been chosen ({len(word)} letters).")
    print(f"  You have {max_wrong} incorrect guesses before it's over.\n")

    while wrong_guesses < max_wrong:
        display_board(wrong_guesses, guessed_letters, word)

        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            print(f"\n  ✅  Good guess! '{guess}' is in the word.")
            if check_win(word, guessed_letters):
                display_board(wrong_guesses, guessed_letters, word)
                print("=" * 45)
                print(f"  🎉  YOU WON! The word was: '{word}'")
                print("=" * 45)
                return
        else:
            wrong_guesses += 1
            print(f"\n  ❌  Wrong! '{guess}' is not in the word. "
                  f"({max_wrong - wrong_guesses} guess(es) remaining)")

    # Game over
    display_board(wrong_guesses, guessed_letters, word)
    print("=" * 45)
    print(f"  💀  GAME OVER! The word was: '{word}'")
    print("=" * 45)


def main():
    while True:
        play_game()
        print()
        again = input("  Play again? (yes / no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\n  Thanks for playing Hangman! Goodbye 👋\n")
            break


if __name__ == "__main__":
    main()
