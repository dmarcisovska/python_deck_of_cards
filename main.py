from random import shuffle
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

    def count(self):
        return len(self.cards)

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def _deal(self, num):
        count = self.count()
        deal_num = min(count, num)
        dealt_cards = []
        if count == 0:
            raise ValueError("All cards have been dealt")
        for i in range(deal_num):
            dealt_cards.append(self.cards.pop())
        return dealt_cards, count

    def deal_card(self):
        return self._deal(1)[0][0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)[0]

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        return shuffle(self.cards)




d = Deck()
d.shuffle()
card = d.deal_card()
hand = d.deal_hand(50)
card2 = d.deal_card()
print(card)
print(card2)
print(hand)
print(d.cards)
# card3 = d.deal_card()







