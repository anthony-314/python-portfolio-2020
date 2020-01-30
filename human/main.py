from RPG_Hero import *
from armor import *

player = Hero()
print(player.inventory)
for i in player.inventory:
    print(i)
player.equipGloves()
print(player.inventory)
print(player.gloves)
print(player.inventory)