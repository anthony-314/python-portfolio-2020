from RPG_Hero import *
from armor import *



def switchTurn(turn):
    if turn == 0:
        turn = 1
        notturn =0
    else:
        turn = 0
        notturn = 1
    return turn, notturn

players=[]
for i in range(2):
    print("create Player", i)
    player = Hero()
    player.equipAll()
    player.append(player)


turn = 0
notturn = 1
while players[0].isAlive:
    print()
    print("its your attack")
    x = players[turn].attack()
    players[notturn].defend(x)
    if players[1].isAlive == False:
        xp, item = players[1].die()
        players[0].addXp(xp)
        players[0].addToInv(item)
        players[0].equipAll()
        print("shorts are the best. do you like shorts")
        player = Hero()
        players[1] = player
    turn, notturn = switchTurn(turn)
print(players[0].name,"has died")

    #switch turns
