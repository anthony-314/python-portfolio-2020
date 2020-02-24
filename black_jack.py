import game as G
import card as C

class BJ_Card(C.Card):
    Ace_value = 1
    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANK.index(self.rank)+1
            if v > 10:
                v = 10
        else:
            v = None
        return v

class BJ_Deck(C.Deck):
    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANK:
                self.cards.append(BJ_Card(rank, suit))


class BJ_Hand(C.Hand):
    """ A Black Jack Hand. """
    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super(BJ_Hand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep
    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                retun None
        t = 0
        for card in self.cards:
            t += card.value

        contains_ace = False
        for card in self.cards:
            if card.value == BJ_Card.Ace_value:
                contains_ace = True
        if contains_ace and t<=11:
            t += 10

        return t

    def is_busted(self):
        return self.total >= 21

class BJ_Player(BJ_Hand):
    def is_hitting(self):
        response = G.ask_yes_no("\n" + self.name+ ", do you want a hit? (y/n):")
        return  response == "y"
    def bust(self):
        print(self.name, "busts")
        self.lose()
    def lose(self):
        print(self.name, "you lose")
    def win(self):
        print(self.name, "Wins!")

    def push(self):
        print(self.name, "pushes.")
class BJ_Dealer(BJ_Player):
    def is_hitting(self):
        return self.total < 17

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()
class BJ_Game(object):
    """A Blackjack game"""
    def __str__(self):
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)
        self.dealer = BJ_Dealer("Dealer")
        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()
    @property
    def still_playing(self):
        sp =[]
        for player in self.players:
            if not player.is_busted:
                sp.append(player)
            return sp
    def __aditional_cards(self,player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()

    def play(self):
        self.deck.deal(self.players + [self.dealer], per_hand = 2)
        self.dealer.flip_first_card()
        for player in self.players:
            print(player)
        print(self.dealer)

        for player in self.players:
            self.__additional_cards(player)

        self.dealer.flip_first_card()

        if not self.still_playing:
            print(self.dealer)
        else:
            print(self.dealer)
            self.__additional_cards(self.dealer)

            if self.dealer.is_busted():
                for player in self.still_playing:
                    player.win()
            else:
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()

        for player in self.players:
         player.clear()
         self.dealer.clear()
def main():
    print("\t\t WELCOME TO BLACKJACK!\n")
    names = []
    number = G.ask_number("How many players? (1-7): ", low = 1, high = 8)
    for i in range(number):
        name = input("Enter you name: ")
        names.append(name)

        again = None
        while again != "n":
            game.play()
            again = G.ask_yes_no("\n Do you want to play again?:")



deck = BJ_Deck()
deck.populate()
deck.shuffle()

print(deck.cards[0])
print(deck.cards[0].value)
deck.cards[0].flip()
print(deck.cards[0])
print(deck.cards[0].value)