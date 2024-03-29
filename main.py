import random
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
                self.cards.append(Card(value, suit))
        # print(self.cards)
        # print(f"Deck of {len(self.cards)} cards")

    def count(self):
        return len(self.cards)

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def deal(self, num):
        count = self.count()
        deal_num = min([count, num])
        dealt_cards = []
        print(f"going to remove {deal_num} cards")
        if count == 0:
            raise ValueError("All cards have been dealt")
        for i in range(deal_num):
            dealt_cards.append(self.cards.pop())
        return dealt_cards, count

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        return random.shuffle(self.cards)



d = Deck()
print(d.deal(3))
print(d.count())






