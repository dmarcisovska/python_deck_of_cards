class Card:
    def __init__(self, suit, value):
        self._suit = suit
        self._value = value

    def __repr__(self):
        return f"{self._value} of {self._suit}"


class Deck:


