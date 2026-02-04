import random
import options
import sys

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n "))
if player_choice > 2 or player_choice < 0:
    print("You typed an invalid number, you lose!")
    sys.exit()
computer_choice = random.randint(0, 2)
print(options.options[player_choice])
print(f"Computer chose:\n{options.options[computer_choice]}")


if player_choice == computer_choice:
    print("It's a draw")
elif(
    (player_choice == 0 and computer_choice == 2) or
    (player_choice == 1 and computer_choice == 0) or
    (player_choice == 2 and computer_choice == 1)
):
    print("You win!")
else:
    print("You lose")