# Day 9: Secret Auction

## 🎯 Project Goal
Create a blind auction program where multiple users can enter their names and bids. The program maintains secrecy by "clearing" the screen through vertical spacing and reveals the highest bidder at the end.

## 🧠 Key Concepts
* **Python Dictionaries**: Storing bidder names as keys and bid amounts as values.
* **Input Validation**: Implementing `while` loops to ensure users enter valid bid amounts and specific "yes/no" responses.
* **Dictionary Iteration**: Writing a custom function to loop through data and calculate the maximum value.
* **The "Vertical Clear" Method**: Using `print("\n" * 100)` to push previous entries out of sight, ensuring a cross-platform "clear" effect.

## 🛠️ How to Use
1. Run `main.py`.
2. Enter your name and a bid (must be greater than $0$).
3. Type 'yes' to clear the terminal for the next bidder, or 'no' to finish.
4. The program automatically formats the final bid for a clean display.

## 📂 File Structure
* `main.py` - Core logic, including the `get_winner` and `secret_auction` functions.
* `art.py` - ASCII art for the Gavel/Auction logo.