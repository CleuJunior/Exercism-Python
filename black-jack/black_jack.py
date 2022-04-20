"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""

CARDS_NIP_VALUES = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10
}


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    return CARDS_NIP_VALUES[card]


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one: str - cards dealt in hand.  See below for values.
    :param card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    if CARDS_NIP_VALUES[card_one] > CARDS_NIP_VALUES[card_two]:
        return card_one

    if CARDS_NIP_VALUES[card_one] < CARDS_NIP_VALUES[card_two]:
        return card_two

    return card_one, card_two


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one: str - card dealt. See below for values.
    :param card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    if card_two == 'A':
        return 1

    return 11 if CARDS_NIP_VALUES[card_one] + CARDS_NIP_VALUES[card_two] <= 10 else 1


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one: str - card dealt. See below for values.
    :param card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    if card_one == 'A' and card_two == 'A':
        return False

    if card_one == 'A' and CARDS_NIP_VALUES[card_two] == 10:
        return True

    if card_two == 'A' and CARDS_NIP_VALUES[card_one] == 10:
        return True

    return False


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one: str - cards dealt.
    :param card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    return CARDS_NIP_VALUES[card_one] == CARDS_NIP_VALUES[card_two]


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one: str - first and second cards in hand.
    :param card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    doubling = CARDS_NIP_VALUES[card_one] + CARDS_NIP_VALUES[card_two]

    if doubling in range(9, 12):
        return True

    return False
