import random


class Equipment (object):
    RARITY = ["Common", "Umcommon", " Rare", "Epic", "Legendary"]
    def __init__(self, eqType):
        self.rarityLevel, self.rareMod = self.pickRare()
        self.eqType = eqType

    def pickRare(self):
        x = random.randint(1,10)
        if x >= 1 and x <= 2:
            return Equipment.RARITY[0], 2
        elif x > 2 and x <= 5:
            return Equipment.RARITY[1], 4
        elif x > 5 and x <= 8:
            return Equipment.RARITY[2], 8
        elif x > 8 and x <= 9:
            return Equipment.RARITY[3], 16
        elif x > 9 and x <= 10:
            return Equipment.RARITY[4], 32





class Armor(Equipment):
    ARMORTYPE = ["Helmet", "Chest", "Legs", "Boots", "Gloves"]

    def __init__(self, atype):
        super(Armor,self). __init__("Armor")
        self.armorType = atype
        self.armor = 0
        self.stamina = 0
        self.agi = 0
        self.iq = 0
        self.luck = 0

    def __str__(self):
        return """
        armorType: {}
        Rarity level: {}
        Armor: {}
        Luck: {}
        Stamina: {}
        iq: {}
        Agililty: {}""".format(self.armorType, self.rarityLevel, self.armor, self.luck, self.stamina, self.iq, self.agi)

class Helm(Armor):
    def __init__(self):
        super(Helm,self). __init__(Armor.ARMORTYPE[0])
        self.armor = random.randint(5, 10)*self.rareMod
        self.stamina = random.randint(0, 8) + self.rareMod
        self.agi = random.randint(0,8) + self.rareMod
        self.iq = random.randint(0, 8) + self.rareMod
        self.luck = random.randint(0 , 8) + self.rareMod
class Gloves(Armor):
    def __init__(self):
        super(Gloves, self).__init__(Armor.ARMORTYPE[4])
        self.armor = random.randint(1, 2) * self.rareMod
        self.stamina = random.randint(0, 1) + self.rareMod
        self.agi = random.randint(0, 10) + self.rareMod
        self.iq = random.randint(0, 3) + self.rareMod
        self.luck = random.randint(0, 1000) + self.rareMod

class Chest(Armor):
    def __init__(self):
        super(Chest, self).__init__(Armor.ARMORTYPE[1])
        self.armor = random.randint(10, 20) * self.rareMod
        self.stamina = random.randint(2, 6) + self.rareMod
        self.agi = random.randint(3, 5) + self.rareMod
        self.iq = random.randint(0, 5) + self.rareMod
        self.luck = random.randint(1, 3) + self.rareMod

class Legs(Armor):
    def __init__(self):
        super(Legs, self).__init__(Armor.ARMORTYPE[2])
        self.armor = random.randint(5, 10) * self.rareMod
        self.stamina = random.randint(2, 6) + self.rareMod
        self.agi = random.randint(3, 5) + self.rareMod
        self.iq = random.randint(1, 2) + self.rareMod
        self.luck = random.randint(0, 4) + self.rareMod
class Boots(Armor):
    def __init__(self):
        super(Boots, self).__init__(Armor.ARMORTYPE[3])
        self.armor = random.randint(0, 8) * self.rareMod
        self.stamina = random.randint(0, 25) + self.rareMod
        self.agi = random.randint(15, 30) + self.rareMod
        self.iq = random.randint(0, 5) + self.rareMod
        self.luck = random.randint(0, 4) + self.rareMod



class Weapon(Equipment):
    WEAPONTYPE = ["Sword", "Axe", "Spear"]

    def __init__(self, wType):
        super(Weapon, self). __init__("Weapon")
        self.weaponType = wType
        self.damage = 0
        self.stamina = 0
        self.luck = 0
        self.iq = 0
        self.agi = 0

    def __str__(self):
        return """
        weaponType: {}
        Rarity Level: {}
        Damage: {}
        Luck: {}
        Iq: {}
        Agility: {}
        """.format(self.weaponType, self.rarityLevel, self.damage, self.luck, self.iq, self.agi)

class Sword(Weapon):
    def __init__(self):
        super(Sword, self).__init__(Weapon.WEAPONTYPE[0])
        self.damage = random.randint(20, 45) * self.rareMod
        self.stamina = random.randint(0, 0) + self.rareMod
        self.luck = random.randint(0, 10) + self.rareMod
        self.iq = random.randint(0, 0) + self.rareMod
        self.agi = random.randint(10, 20) + self.rareMod

class Axe(Weapon):
    def __init__(self):
        super(Axe, self).__init__(Weapon.WEAPONTYPE[1])
        self.damage = random.randint(30, 60) * self.rareMod
        self.stamina = random.randint(0, 0) + self.rareMod
        self.luck = random.randint(0, 0) + self.rareMod
        self.iq = random.randint(0, 0) + self.rareMod
        self.agi = random.randint(0, 0) + self.rareMod
class Spear(Weapon):
    def __init__(self):
        super(Spear, self).__init__(Weapon.WEAPONTYPE[0])
        self.damage = random.randint(10, 25) * self.rareMod
        self.stamina = random.randint(10, 15) + self.rareMod
        self.luck = random.randint(15, 30) + self.rareMod
        self.iq = random.randint(15, 20) + self.rareMod
        self.agi = random.randint(15, 20) + self.rareMod

