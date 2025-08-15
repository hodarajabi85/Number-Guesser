# 🎯 Number Guessing Game (Python)

A simple terminal-based number guessing game written in Python.  
The computer picks a random number between **1** and **100**, and you try to guess it.  
Your score starts at **100** and drops by **10** for each wrong guess.  
You can quit at any time by typing `q`.

---

## 📜 Features
- Random number generation between **1 and 100**
- Score system (starts at 100, loses points for wrong guesses)
- Hint system:
  - **"Too high"** if your guess is above the number
  - **"Too low"** if your guess is below the number
- Option to quit at any time
- Option to replay after each round

---

## 🛠 Requirements
- Python **3.6+**

No external libraries are required — just the built-in Python `random` module.

---

## 🚀 How to Run

1. **Clone or download** this repository.
2. Open a terminal in the project folder.
3. Run the script:

```bash
python guessing_game.py
```
## 🎮 How to Play
1.The game will choose a random number between 1 and 100.

2.Enter your guess in the terminal.

3.You’ll be told if your guess is too high or too low.

- Keep guessing until:

- You guess the correct number 🎉

4. You type q to quit

5. Your score decreases by 10 for each wrong guess.

6. After each round, you can choose to play again or exit.

---

## 📂 File Structure

|--guessing_game.py   # Main game script
|--README.md          # This file

## 🖊 Example Game Play
Please enter your guess number (between 1 and 100) or 'q' to quit: 50
It is much higher than my choice. Please try again.
Please enter your guess number (between 1 and 100) or 'q' to quit: 25
It is much lower than my choice. Please try again.
Please enter your guess number (between 1 and 100) or 'q' to quit: 37
You win!
Your score is: 80
Would you like to play again? (yes/no): no
Thanks for playing. Goodbye!

---

## 📄 License
This project is licensed under the MIT License.
You are free to use, modify, and distribute it for personal or commercial purposes.

---

## ✨ Author
Made with ❤️ in Python by HODA RAJABI

---
