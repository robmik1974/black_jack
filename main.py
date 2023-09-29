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

print(calculate_score(user_cards))
print(calculate_score(computer_cards))
