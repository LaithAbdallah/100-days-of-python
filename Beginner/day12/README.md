# Day 12: Number Guessing Game

## 🎯 Project Goal
Create a game where the computer selects a random number between 1 and 100, and the player has a limited number of attempts to guess it based on a chosen difficulty level.

## 🧠 Topics Covered
* **Local vs. Global Scope**: Understanding the boundaries of where variables can be accessed and modified.
* **Global Constants**: Using uppercase naming conventions (e.g., `EASY_LEVEL_TURNS = 10`) for variables that never change.
* **Namespace**: Learning how Python searches for variable names in different "levels" of the code.
* **The `global` Keyword**: Why it's generally avoided and how to modify global variables safely by using `return`.

## 🛠️ How to Play
1. Run `main.py`.
2. Choose a difficulty: 'easy' (10 attempts) or 'hard' (5 attempts).
3. Guess a number between 1 and 100.
4. The game will tell you if your guess is "Too high" or "Too low" and update your remaining attempts.

## 📂 File Structure
* `main.py` - Core game logic including the guess-checking function and the game loop.
* `art.py` - ASCII art for the game logo.