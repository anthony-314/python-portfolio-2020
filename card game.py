import card

def get_name():
    name = ''
    while name == "":
        name = input("enter your user name and password")
    return name


total_players = int(input("how many people are playing? #?"))
names = []
hands = []
for i in range(total_players):
    x = get_name()
    hand = card.Hand()
    hands.append(hand)
    names.append(x)
deck = card.Deck()
deck.populate()
deck.shuffle()
deck.deal(hands, 1)

for hand in hands:
    print(hand)




