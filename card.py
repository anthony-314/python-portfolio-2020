import random
class Card(object):
    RANK = ("A", "2", "3", '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K' )
    SUITS = ("♠", "♥", "♦", "♣",)

    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        rep = str.format("""
        --------
        | {0}    |
        | {1}    |
        |    {1} |
        |    {0} |
        --------
        """, self.rank,self.suit)
        return rep
class Hand(object):
    def __init__(self):
        self.cards = []
    def __str__(self):
        if self.cards:
            rep = " "
            for card in self.cards:
                rep += str(card)+""

        else:
            rep = "Empty"
        return rep
    def clear(self):
        self.cards =[]
    def add(self, card):
        self.cards.append(card)
    def give(self, other_hand, card):
        self.cards.remove(card)
        other_hand.add(card)

my_hand = Hand()
your_hand = Hand()
for i in range(5):
    card = Card(random.choice(Card.RANK), random.choice(Card.SUITS))
    my_hand.add(card)

print(my_hand)
print(your_hand)
my_hand.give(your_hand, my_hand.cards[0])
print(your_hand)
my_hand.clear()
your_hand.clear()
print(my_hand)
print(your_hand)