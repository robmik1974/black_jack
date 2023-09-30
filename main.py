## Our Blackjack House Rules ##

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random


def deal_cards() -> int:
    """Function that uses the list of cards to return a random card."""
    cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

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


user_cards = []
computer_cards = []

for _ in range(2):
    user_cards.append(deal_cards())
    computer_cards.append(deal_cards())

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)
print(f"User score: {user_score}")
print(f"Computer score: {computer_score}")

STOP_CONTINUE = False

while not STOP_CONTINUE:
    if user_score == 0 or computer_score == 0 or user_score > 21:
        STOP_CONTINUE = True
    else:
        if input("Do you want to draw another card?").lower() == "y":
            user_cards.append(deal_cards())
            user_score = calculate_score(user_cards)
            print(f"User score: {user_score}")
            print(f"Computer score: {computer_score}")
        else:
            while not STOP_CONTINUE:
                if computer_score < 17:
                    computer_cards.append(deal_cards())
                    computer_score = calculate_score(computer_cards)
                    print(f"User score: {user_score}")
                    print(f"Computer score: {computer_score}")
                else:
                    STOP_CONTINUE = True


print(f"User score: {user_score}")
print(f"Computer score: {computer_score}")
