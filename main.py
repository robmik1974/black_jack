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
        score = 0
    if 11 in list_of_cards:
        if score > 21:
            list_of_cards.remove(11)
            list_of_cards.append(1)
            score = sum(list_of_cards)
    return score


def compare(user: int, computer: int) -> str:
    """Function passes in the user_score and computer_score and calculates game result"""
    game_result = ""
    if user == computer:
        game_result = "Draw 🤪"
    elif computer == 0:
        game_result = "Lose, opponent had Blackjack 😱"
    elif user == 0:
        game_result = "Win with a Blackjack 😎"
    elif computer > 21:
        game_result = "Opponent went over. You win 😁"
    elif user > 21:
        game_result = "You went over. You lose 😭"
    elif user > computer:
        game_result = "You win 😄"
    else:
        game_result = "You lose 😤"
    return game_result


def play_game() -> None:
    """Main logic of the Blackjack game"""
    print(LOGO)

    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your hand: {user_cards}, current score: {user_score}")
    print(f"Computer's hand: [{computer_cards[0]}, ?]")

    stop_deal = False

    while not stop_deal:
        if user_score == 0 or computer_score == 0 or user_score > 21:
            stop_deal = True
        else:
            if input("Type 'y' to get another card, type 'n' to pass: ").lower() == "y":
                user_cards.append(deal_cards())
                user_score = calculate_score(user_cards)
                print(f"Your hand: {user_cards}, current score: {user_score}")
            else:
                while computer_score < 17:
                    computer_cards.append(deal_cards())
                    computer_score = calculate_score(computer_cards)
                stop_deal = True

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user=user_score, computer=computer_score))


while input("Do you want play a game of Blackjack. Type [y/n]: ").lower() == "y":
    os.system("clear")
    play_game()
