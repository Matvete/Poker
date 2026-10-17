from enum import Enum


class Suit(Enum):
    CLUB = "♧"
    DIAMOND = "♢"
    HEART = "♡"
    SPADE = "♤"

class CardValue(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

def get_card_value_by_value(value: int):
    return {2: CardValue.TWO,
            3: CardValue.THREE,
            4: CardValue.FOUR,
            5: CardValue.FIVE,
            6: CardValue.SIX,
            7: CardValue.SEVEN,
            8: CardValue.EIGHT,
            9: CardValue.NINE,
            10: CardValue.TEN,
            11: CardValue.JACK,
            12: CardValue.QUEEN,
            13: CardValue.KING,
            14: CardValue.ACE}[value]

class Card:
    def __init__(self, value: CardValue, suit: Suit):
        self.value = value
        self.suit = suit


    def __str__(self) -> str:
        figures = {11:"J", 12:"Q", 13:"K", 14:"A"}
        return f"{figures.get(self.value.value,self.value.value)} {self.suit.value}"