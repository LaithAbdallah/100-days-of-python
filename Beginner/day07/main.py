import random
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6
chosen_word = random.choice(word_list)
print(logo)

placeholder = "_" * len(chosen_word)
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
display = ""
tries = 0
while not game_over:
    if display != chosen_word and tries > 0:
        print(f"**************************** {lives}/6 Lives Left ****************************")
        print("Word to guess: " + display)
    tries += 1
    guess = input("Guess a letter: ").lower()

    display = ""
    if guess in correct_letters:
        print(f"You've already guessed {guess}")
    for letter in chosen_word:
        if letter == guess or letter in correct_letters:
            display += letter
            if letter not in correct_letters:
                correct_letters.append(letter)
        else:
            display += "_"

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f"*********************** It Was {chosen_word}! You Lose **********************")

    if "_" not in display:
        game_over = True
        print(chosen_word)
        print("**************************** You Win ****************************")

    if not game_over:
        print(stages[lives], end = "")
