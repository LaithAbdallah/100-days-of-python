import art
import random

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

def check_answer(number, attempts):
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == number:
        return "win"
    elif attempts == 1:
        return attempts - 1
    elif guess < number:
        print("Too low.\nGuess again.")
    elif guess > number:
        print("Too high.\nGuess again.")
    return attempts - 1

def game(diff, num):
    if diff == "hard":
        attempts = HARD_ATTEMPTS
    else:
        attempts = EASY_ATTEMPTS
    while attempts:
        attempts = check_answer(num, attempts)
        if attempts == "win":
            return True

    return False

def main():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = random.randint(1,100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    while difficulty not in ["easy", "hard"]:
        difficulty = input("Please choose either 'easy' or 'hard': ").lower()
    state = game(difficulty, number)
    if state:
        print(f"You got it! The answer was {number}.")
    else:
        print("You've run out of guesses.")

if __name__ == "__main__":
    main()