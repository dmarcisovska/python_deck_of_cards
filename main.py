class Card:
    def __init__(self, value, suit):
        self._value = value
        self._suit = suit

    def __repr__(self):
        return f"{self._value} of {self._suit}"


# class Deck:

c = Card("A", "Hearts")
print(c)


