import random
from turtle import clear 

inp1 = input("Do you want to play a black jack game? 'y' for yes, 'n' for no " )

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(List_of_cards):

    if sum(List_of_cards) == 21 and len(List_of_cards) == 2:
        return 0
    
    if 11 in List_of_cards and sum(List_of_cards) > 21:
        List_of_cards.remove(11)
        List_of_cards.append(1)

    return sum(List_of_cards)

def compare(user_scores, computer_scores):
    if user_scores == computer_scores:
        return "Draw"
    elif computer_scores == 0:
        return "Lose, opponent has Blackjack"
    elif user_scores == 0:
        return "Win, with a Blackjack"
    elif user_scores > 21:
        return "You went over. You loose"
    elif computer_scores > 21:
        return "You win"
    else:
        return "You lose"

def play_game():
    user_cards = []
    computer_cards = []
    user_scores = 0
    computer_scores = 0
    is_game_over = False


    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while (not is_game_over):
        user_scores = calculate_score(List_of_cards = user_cards)
        computer_scores = calculate_score(List_of_cards = computer_cards)

        if user_scores == 0 or computer_scores == 0 or user_scores > 21:
            is_game_over = True
        else:
            inp = input("Type 'y' to get another card, type 'n' to pass: ")
            if (inp == 'y'):
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while (computer_scores != 0 and computer_scores < 17):
        computer_cards.append(deal_card())
        computer_scores = calculate_score(List_of_cards = computer_cards)

    print(f"  Your final hand: {user_cards}, final score: {user_scores}")
    print(f"  Computer's final hand: {computer_cards}, final score: {computer_scores}")
    print(compare(user_scores, computer_scores))

while(input("Do you want to play a game of Blackjack? (y/n): ") == "y"):
    clear()
    play_game()