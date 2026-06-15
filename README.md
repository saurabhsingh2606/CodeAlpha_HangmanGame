# 🎮 Hangman Game — CodeAlpha Internship Task 1

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Internship-CodeAlpha-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Task-1%20of%204-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Type-Console%20Game-purple?style=for-the-badge" />
</p>

---

## 📌 About the Project

A classic **text-based Hangman Game** built in Python as part of the **CodeAlpha Python Programming Internship**.  
The player guesses a hidden word one letter at a time, with a maximum of **6 incorrect guesses** before the hangman is fully drawn and the game ends.

---

## 🕹️ How to Play

```
1. A random secret word is chosen from a predefined list.
2. You see blanks representing each letter: _ _ _ _ _ _
3. Guess one letter at a time.
4. ✅ Correct guess → the letter is revealed in the word.
5. ❌ Wrong guess   → the hangman drawing grows (max 6 wrong).
6. 🎉 Win  → guess all letters before 6 wrong guesses.
7. 💀 Lose → 6 wrong guesses and the hangman is complete.
```

---

## 🖥️ Demo Preview

```
=============================================
         🎮  WELCOME TO HANGMAN!  🎮
=============================================
  A random word has been chosen (6 letters).
  You have 6 incorrect guesses before it's over.

       ------
       |    |
       |    O
       |   /|\
       |   /
       |
    --------

  Wrong guesses left : 1
  Letters guessed    : a, e, p, t, y, z

  Word: p y t _ _ _

  Guess a letter: h
  ✅  Good guess! 'h' is in the word.
```

---

## ✨ Features

- 🎲 **Random Word Selection** — picks from 5 built-in words every game
- 💀 **ASCII Hangman Art** — 7 progressive stages drawn in the console
- ✅ **Input Validation** — rejects numbers, symbols, multi-characters & repeated guesses
- 🔁 **Play Again Option** — replay without restarting the program
- 🏆 **Win / Lose Detection** — announces result and reveals the secret word

---

## 📂 Project Structure

```
CodeAlpha_HangmanGame/
│
├── hangman.py       ← Main game file
└── README.md        ← Project documentation
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed → [Download here](https://python.org)

### Run the Game

```bash
# Clone the repository
git clone https://github.com/YourUsername/CodeAlpha_HangmanGame.git

# Navigate into the folder
cd CodeAlpha_HangmanGame

# Run the game
python hangman.py
```

---

## 🧠 Concepts & Technologies Used

| Concept | Usage |
|---|---|
| `random` module | Randomly selects a word each game |
| `while` loop | Keeps the game running until win or loss |
| `if-else` statements | Checks correct/wrong guesses & conditions |
| `set` | Stores guessed letters (no duplicates) |
| `functions` | Modular code — display, input, win-check |
| `f-strings` | Clean, formatted console output |
| `list indexing` | Selects correct ASCII hangman stage |

---

## 📋 Word List

The game currently uses these 5 predefined words:

```python
WORDS = ["python", "developer", "hangman", "keyboard", "algorithm"]
```

---

## 🔮 Future Improvements

- [ ] Add more words or load from a `.txt` file
- [ ] Add difficulty levels (Easy / Medium / Hard)
- [ ] Track high scores across sessions
- [ ] Build a GUI version using `tkinter`
- [ ] Add hint system

---

## 👨‍💻 Author

**Your Name**  
🔗 [LinkedIn](https://linkedin.com/in/yourprofile)  
🐙 [GitHub](https://github.com/YourUsername)  

---

## 🏢 Internship

This project was built as **Task 1** of the **Python Programming Internship** at  
**[CodeAlpha](https://www.codealpha.tech)** — A leading software development company.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<p align="center">
  Made with ❤️ during CodeAlpha Python Internship
</p