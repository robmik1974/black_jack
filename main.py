"""Simple Black Jack game"""

import random
import os
from art import LOGO


def deal_cards() -> int:
    """Function that uses the list of cards to return a random card."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    return random.choice(cards)


def calculate_score(list_of_cards: list[int]) -> int:
    """Function takes a ist of cards as input and returns the score."""
    score = sum(list_of_cards)
    if len(list_of_cards) == 2 and score == 21:
        return 0
    if 11 in list_of_cards:
        if score > 21:
            list_of_cards.remove(11)
            list_of_cards.append(1)
            return sum(list_of_cards)
    return score


def compare(user: int, computer: int) -> str:
    """Function passes in the user_score and computer_score and calculates game result"""
    game_result = ""
    if user == computer:
        game_result = "It's draw"
    elif computer == 0 or user > 21:
        game_result = "You lose"
    elif user == 0 or computer_score > 21:
        game_result = "You won"
    else:
        if user > computer:
            game_result = "You win"
        else:
            game_result = "You lose"
    return game_result


STOP_CONTINUE = False
while not STOP_CONTINUE:
    os.system("clear")
    print(LOGO)

    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your hand: {user_cards}")
    print(f"Computer's hand: [{computer_cards[0]}, ?]")

    STOP_DEAL = False

    while not STOP_DEAL:
        if user_score == 0 or computer_score == 0 or user_score > 21:
            STOP_DEAL = True
        else:
            if input("Do you want to draw another card ?: ").lower() == "y":
                user_cards.append(deal_cards())
                user_score = calculate_score(user_cards)
                print(f"Your hand: {user_cards}")
            else:
                while not STOP_DEAL:
                    if computer_score < 17:
                        computer_cards.append(deal_cards())
                        computer_score = calculate_score(computer_cards)
                    else:
                        STOP_DEAL = True
    print(f"Computer hand: {computer_cards}")
    print(f"Your score: {user_score}")
    print(f"Computer's score: {computer_score}")
    print(compare(user=user_score, computer=computer_score))

    if input("Do you want play again [y/n] ?: ").lower() == "n":
        STOP_CONTINUE = True
