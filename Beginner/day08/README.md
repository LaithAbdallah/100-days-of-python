# Day 8: Caesar Cipher

## 🎯 Project Goal
Develop a tool that encrypts and decrypts text using the Caesar Cipher method, shifting letters of the alphabet by a user-defined number.

## 🧠 Key Concepts
* **Functions with Parameters**: Passing multiple pieces of data (text, shift, direction) into a single function.
* **Positional vs. Keyword Arguments**: Understanding the difference between `function(a, b)` and `function(b=1, a=2)`.
* **Modulo Operator (%)**: Using math to ensure shifts stay within the 26-letter alphabet range.
* **User Experience**: Implementing a loop to allow the user to restart the program without exiting.

## 🛠️ How to Use
1. Run `main.py`.
2. Choose `encode` to encrypt a message or `decode` to decrypt one.
3. Input your message and the numerical shift value.
4. The program will handle symbols, numbers, and spaces automatically while only shifting letters.

## 📂 File Structure
* `main.py` - The core logic for the cipher and the game loop.
* `art.py` - ASCII art for the project logo.