from RPG_Hero import *

player = Hero()
print(player)
while player.level <5 :
    xp = random.randint(10,50)
    player.addXp(xp)
