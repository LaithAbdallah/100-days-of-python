import art
import random

def input_validator(prompt):
    decision = input(prompt).lower()
    while decision not in ['y','n']:
        decision = input("Please choose either 'y' or 'n' only: ").lower()
    return decision

def add_random_card(lst, score,  cards):
    choice = random.choice(cards)
    # ace can be either 1 or 11
    if choice == 11:
        if score + 11 > 21:
            lst.append(1)
            score += 1
        else:
            lst.append(11)
            score += 11
    else:
        lst.append(choice)
        score += choice
    # if ace exists, and we add a new card that makes score > 21, we change the ace to 1
    if score > 21 and 11 in lst:
        lst[lst.index(11)] = 1
        score -= 10
    return score

def blackjack(cards):
    print(art.logo)
    user_cards = []
    computer_cards = []
    user_score = 0
    computer_score = 0
    computer_score = add_random_card(computer_cards, computer_score,cards)
    user_score = add_random_card(user_cards, user_score, cards)
    user_score = add_random_card(user_cards, user_score, cards)
    print(f"    Your cards: {user_cards}, current score:{user_score}")
    print(f"    Computer's first card: {computer_cards[0]}")
    while user_score < 21 and computer_score < 21:
        hit_or_stand = input_validator("Type 'y' to get another card, type 'n' to pass: ")
        if hit_or_stand == 'y':
            user_score = add_random_card(user_cards, user_score, cards)
            print(f"    Your cards: {user_cards}, current score: {user_score}")
            print(f"    Computer's first card: {computer_cards[0]}")
            if user_score > 21:
                break
        else:
            while computer_score < 17:
                computer_score = add_random_card(computer_cards, computer_score,cards)
            break
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    if user_score > 21:
        print("You went over. You lose 😭")
    elif computer_score > 21:
        print("Opponent went over. You win 😁")
    elif computer_score > user_score and computer_score == 21 and len(computer_cards) == 2:
        print("Lose, opponent has Blackjack 😱")
    elif user_score > computer_score and user_score == 21 and len(user_cards) == 2:
        print("Win with a Blackjack 😎")
    elif user_score > computer_score:
        print("You win 😃")
    elif computer_score > user_score:
        print("You lose 😤")
    else:
        print("Draw 🙃")

def main():
    # The jack, queen and king all count as 10
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    while True:
        new_game = input_validator("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if new_game == 'y':
            blackjack(cards)
        else:
            break

if __name__ == "__main__":
    main()