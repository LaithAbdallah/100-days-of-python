# Day 11: Blackjack Capstone

## 🎯 Project Goal
The first Capstone project! The goal was to build a fully functional, automated Blackjack game. This required coordinating multiple functions, managing a complex game state, and implementing specific casino rules (like the Dealer hitting until 17 and the Ace value adjustment).

## 🧠 Topics Covered
* **Capstone Logic**: Combining all skills from the first 10 days (Loops, Functions with Outputs, Dictionaries, and Conditionals).
* **Game State Management**: Tracking the status of the game (Is it over? Who wins?) across multiple turns.
* **Complex Conditionals**: Handling the "Ace" logic (1 or 11) and the Blackjack (Score 21 with 2 cards) edge cases.
* **The "Dealer" AI**: Automating the computer's decisions based on fixed rules.

## 🛠️ Features
* **Dynamic Deck**: Cards are dealt and scores are updated in real-time.
* **Ace Handling**: Automatically converts an Ace from 11 to 1 if the player's score exceeds 21.
* **Casino Rules**: Dealer must hit until their score is at least 17.
* **Recursive Gameplay**: Option to restart a new game immediately after the previous one ends.

## 📂 File Structure
* `main.py` - The core game engine and logic flow.
* `art.py` - ASCII art for the Blackjack logo.