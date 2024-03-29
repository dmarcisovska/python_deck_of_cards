class Card:
    def __init__(self, value, suit):
        self._value = value
        self._suit = suit

    def __repr__(self):
        return f"{self._value} of {self._suit}"


class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.cards = []
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))
        print(self.cards)
        print(f"Deck of {len(self.cards)} cards")

    def __repr__(self):
        return f"Deck of {len(self.cards)} cards"

    def deal(self, num):
        for i in range(num):
            self.cards.pop()



Deck()






