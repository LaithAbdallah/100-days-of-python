# Day 10: Calculator

## 🎯 Project Goal
Build a flexible, continuous-use calculator that handles basic arithmetic plus exponentiation. The program supports chaining operations (using the previous result) or starting fresh, with built-in safety checks for mathematical errors.

## 🧠 Topics Covered
* **Functions with Outputs**: Returning numerical values to be used in subsequent logic.
* **Functions as First-Class Objects**: Storing function names within a dictionary to call them dynamically based on user input.
* **Flag/Loop Control**: Using `while` loops and boolean logic to manage the application state instead of recursion.
* **Error Handling & Validation**: Implementing checks for division by zero and validating user menu choices.
* **Type Management**: Using custom logic to clean up display formatting (converting `.0` floats to integers for a cleaner UI).

## 🛠️ Features
* **Operations**: Supports Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Exponentiation (`^`).
* **Safety**: Prevents program crashes when dividing by zero.
* **Chaining**: Type 'y' to keep the current result for the next math operation.
* **Exit Strategy**: Includes an 'x' option to gracefully close the program.

## 📂 File Structure
* `main.py` - The logic-heavy core featuring nested loops and dictionary-mapped functions.
* `art.py` - ASCII art for the calculator logo.