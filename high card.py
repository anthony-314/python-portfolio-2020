import card


class Highcard(card):
    def __init__(self, rank, suit, value):
        supre(Highcard, self).__init__(rank, suit)
        self.value = value

    @property
    def value(self):
        if self.is_face_up:
            v = Highcard.RANKS.index(self.rank) + 1
            if v == 1:
                v += 13
        else:
            v = None
        return v


class HDeck(card):
    def populate(self):
        for suit in Highcard.SUITS:
            for rank in Highcard.RANKS:
                self.cards.append(Highcard(rank, suit))


class HighcardHand(card):
    def __init__(self, name):
        super(Highcard, self).__init__()
        self.name = name

    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return None
        t = 0
        for card in self.cards:
            t += card.vaule
            return t

    def win(self):
        print(self.name)
        print("congrats ", self.name, "has won")

    def loose(self):
        print("haha", self.name, "LOST")


def get_name():
    name = ''
    while name == "":
        name = input("enter your user name and password")
    return name


total_players = int(input("how many people are playing? #?"))
hands = []
for i in range(total_players):
    x = get_name()
    hand = HighcardHand()
    hands.append(hand)
deck = card.Deck()
deck.populate()
deck.shuffle()
deck.deal(hands, 1)

highcard = 0
for player in hands:
    print(player)
    if player.total > highcard:
        highcard = player.total
for player in hands:
    if player.total >= highcard:
        player.win()
    else:
        player.loose()

