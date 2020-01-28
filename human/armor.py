import random


class Equipment (object):
    RARITY = ["Common", "Umcommon", " Rare", "Epic", "Legendary"]
    def __init__(self, eqType):
        self.rarityLevel = self.pickRare()
        self.eqType = epType

    def pickRare(self):
        x = random.randint(1,10)
        if x >= 1 and x <= 2:
            return Equipment.RARITY[0]
        elif x > 2 and x < 5:
            return Equipment.RARITY[1]




class Armor(Equipment):
    ARMORTYPE = ["Helmet", "Chest", "Legs", "Boots", "Gloves"]

    def __init__(self):
        super(Armor,self). __init__("Armor")

class Weapon(Equipment):
    WEAPONTYPE = []

    def __init__(self):
        super(Weapon,self). __init__("Weapon")
