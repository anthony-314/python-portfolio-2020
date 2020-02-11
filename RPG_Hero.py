import random
from armor import *

class Hero(object):
    raceList = ["Human","Elf","Dwarf", "K9"]
    classList = ["Warrior","Mage","Hunter","Dog","Karen"]
    def __init__(self):
        self.isAlive = True
        self.name = ""
        self.name = self.enterName()
        self.race = self.pickRace()
        self.playerClass = self.pickClass()
        self.level = 1
        self.xp = 0
        self.levelUp = (self.level*10)+90
        self.healthMod = 10

        self.deff = 0
        self.atk = 0
        self.manaMod = 10
        self.luck = 0
        self.stamina = 0
        self.iq= 0
        self.agi = 0
        self.atklist = []
        self.setMods()




        self.inventory =[]
        self.inventoryMax = 10
        self.helm = []
        self.chest = []
        self.legs=[]
        self.boots=[]
        self.gloves = []
        self.rightHand = []
        self.leftHand = []
        self.popInv()

    def popInv(self):
        x = random.randint(0,3)
        for i in range(x):
            self.addToInv("Health Potion")
        x = random.randint(0,3)
        for i in range(x):
            self.addToInv("Mana potions")

        helm = Helm()
        chest = Chest()
        legs = Legs()
        boots = Boots()
        gloves = Gloves()


        self.addToInv(helm)
        self.addToInv(chest)
        self.addToInv(legs)
        self.addToInv(boots)
        self.addToInv(gloves)
        x = random.randint(0,2)

        if x == 0:
            weapon = Sword()
        elif x == 1:
            weapon = Axe()
        else:
            weapon = Spear()

    def addToInv(self, item):
        if len(self.inventory) < self.inventoryMax:
            self.inventory.append(item)

        else:
            print("you have to many items in your inventory")
            return



        self.maxHealth = self.level * self.healthMod
        self.currHealth = self.maxHealth
        self.maxMana = self.level * self.manaMod
        self.currMana = self.maxMana

    def pickRace(self):
        while True:
            try:
                print(Hero.raceList)
                x = input("choose your race").title()
                if x in Hero.raceList:
                    return x
            except:
                self.race = random.choice(Hero.raceList)

    def pickClass(self):
        while True:
            try:
                print(Hero.classList)
                x = input("pick your class").title()
                if x in Hero.classList:
                    return x
            except:
                self.playerClass = random.choice(Hero.classList)

    def enterName(self):
        name =""
        while name =="":
            name = input("what would you like to name this character")
            return name

    def setMods(self):
        if self.playerClass == "Warrior":
            self.atklist = ["normal", "med", "strong"]
            self.stamina = random.randint(15, 20)
            self.agi = random.randint(3, 6)
            self.iq = random.randint(7, 12)
            self.deff = random.randint(5,7)
            self.atk = random.randint(8, 12)
            self.luck = random.randint(4 , 6)
        if self.playerClass == "Mage":
            self.atklist = ["normal", 'med', "strong"]
            self.stamina = random.randint(8, 12)
            self.agi = random.randint(3, 4)
            self.iq = random.randint(25, 35)
            self.deff = random.randint(1 , 2)
            self.atk = random .randint(6, 12)
            self.luck = random.randint(10, 15)
        if self.playerClass == "Hunter":
            self.atklist = ["normal", 'med', "strong"]
            self.stamina = random.randint(10, 12)
            self.agi = random.randint(15, 20 )
            self.iq = random.randint(20, 22)
            self.deff = random.randint(10, 24)
            self.atk = random.randint(8, 12)
            self.luck = random.randint(5, 10)
        if self.playerClass == "Dog":
            self.atklist = ["normal", 'med', "strong"]
            self.stamina = random.randint(20, 20)
            self.agi = random.randint(20, 20)
            self.iq = random.randint(20, 20)
            self.deff = random.randint(20, 20)
            self.atk = random.randint(20, 20)
            self.luck = random.randint(20, 20)
        if self.playerClass == "Karen":
            self.stamina = random.randint(1, 2)
            self.agi = random.randint(1, 2)
            self.iq = random.randint(1, 2)
            self.deff = random.randint(1, 2)
            self.atk = random.randint(1, 2)
            self.luck = random.randint(1,2)

    def die(self,champ):
        dropxp = 10 * self.level
        champ.givexp(dropxp)
        item = random.choice(self.inventory)
        champ.giveItem(item)

    def levelUpfun(self):
        if self.xp >= self.levelUp:
            self.level += 1
            print("ding you leveled up")
            remanxp = self.xp - self.levelUp
            self.xp = remanxp
            self.leveUp = 90 + (self.level * 10)
            self.healthMod += self.level
            self.maxHealth = self.level* self.healthMod
            self.currHealth = self.maxHealth
            if self.playerClass != "Warrior":
                self.manaMod += self.level
                self.maxMana = self.level *self.maxMana
                self.currMana = self.maxMana
            self.inreaseMod()

    def inreaseMod(self):
        points = random.randint(1,self.level//2)
        while points > 0:
            print("""
            Luck:{} 
            Stamina:{} 
            Iq:{} 
            Agility: {}
            """.format(self.luck,self.stamina,self.iq,self.agi))
            x = input("what stat would you like to add points to")
            y = 0
            while y == 0:
                try:
                    y = int(input("you have" + str(points)+ " points to spend how many would you like to put in "+ x))
                except:
                    print("that wasn't a good number")
                    y = 0
        if y<= points:
            if x == "Stamina":
                self.stamina += y
                points -= y
            elif x == "Luck":
                self.luck += y
                points -= y
            elif x == "Iq":
                self.iq += y
                points -= y
            elif x == "Agility":
                self.agi += y
                points -= 1
            else:
                print("not an valid")
        else: print("You don't have that many points")

    def addXp (self,xp):
        print("picked up " + str(xp) +"xp")
        self.xp += xp
        if self.xp >= self.levelUp:
            self.levelUpfun()

    def __str__(self):
        return"""
        Name: {} \t Race:{} \t Class {} \t Level: {}
        Attack: {}
        Deffence: {}
        Luck: {}
        Stamina: {}
        Iq: {}
        Agility:{}""" .format(self.name,self.race,self.playerClass,self.level,self.atk,self.deff,self.luck,self.stamina,self.iq,self.agi)

    def equipGloves(self):
        for i in self.inventory:
            x = type(i)
            if "Gloves" in str(x):
                if len(self.gloves) < 1:
                    for i in self.inventory:
                        x = type(i)
                        if "Gloves" in str(x):
                            print("you equipped a set of gloves")
                            print(i)
                            self.gloves.append(i)
                            self.inventory.remove(i)
                            self.deff += self.gloves[0].armor
                            self.luck += self.gloves[0].luck
                            self.stamina += self.gloves[0].stamina
                            self.iq += self.gloves[0].iq
                            self.agi += self.gloves[0].agi
                else:
                    print("you need to remove equipped gloves first")
                    print(self.gloves[0])
                    print("would you like to replace them")
                    print(i)
                    while True:
                        x = input("yes or no")
                        if x == "yes":
                            print("you replaced gloves")
                            self.deff -= self.gloves[0].armor
                            self.luck -= self.gloves[0].luck
                            self.stamina -= self.gloves[0].stamina
                            self.iq -= self.gloves[0].iq
                            self.agi -= self.gloves[0].agi
                            self.gloves.remove(self.gloves[0])
                            self.gloves.append(i)
                            self.inventory.remove(i)
                            self.deff += self.gloves[0].armor
                            self.luck += self.gloves[0].luck
                            self.stamina += self.gloves[0].stamina
                            self.iq += self.gloves[0].iq
                            self.agi += self.gloves[0].agi
                            break
                        elif x == "no":
                            self.inventory.remove(i)
                            break

    def equipHead(self):

        for i in self.inventory:
            x = type(i)
            if "Helm" in str(x):
                if len(self.helm) < 1:
                    for i in self.inventory:
                        x = type(i)
                        if "Helm" in str(x):
                            print("you equipped a helm")
                            print(i)
                            self.helm.append(i)
                            self.inventory.remove(i)
                            self.deff += self.helm[0].armor
                            self.luck += self.helm[0].luck
                            self.stamina += self.helm[0].stamina
                            self.iq += self.helm[0].iq
                            self.agi += self.helm[0].agi
                else:
                    print("you need to remove equipped helm first")
                    print(self.helm[0])
                    print("would you like to replace them")
                    print(i)
                    while True:
                        x = input("yes or no")
                        if x == "yes":
                            print("you replaced helm")
                            self.deff -= self.helm[0].armor
                            self.luck -= self.helm[0].luck
                            self.stamina -= self.helm[0].stamina
                            self.iq -= self.helm[0].iq
                            self.agi -= self.helm[0].agi
                            self.helm.remove(self.helm[0])
                            self.helm.append(i)
                            self.inventory.remove(i)
                            self.deff += self.helm[0].armor
                            self.luck += self.helm[0].luck
                            self.stamina += self.helm[0].stamina
                            self.iq += self.helm[0].iq
                            self.agi += self.helm[0].agi
                            break
                        elif x == "no":
                            self.inventory.remove(i)
                            break

    def equipChest(self):
        for i in self.inventory:
            x = type(i)
            if "Chest" in str(x):
                if len(self.chest) < 1:
                    for i in self.inventory:
                        x = type(i)
                        if "Chest" in str(x):
                            print("you equipped chest armor")
                            print(i)
                            self.chest.append(i)
                            self.inventory.remove(i)
                            self.deff += self.chest[0].armor
                            self.luck += self.chest[0].luck
                            self.stamina += self.chest[0].stamina
                            self.iq += self.chest[0].iq
                            self.agi += self.chest[0].agi
                else:
                    print("you need to remove equipped chest first")
                    print(self.chest[0])
                    print("would you like to replace them")
                    print(i)
                    while True:
                        x = input("yes or no")
                        if x == "yes":
                            print("you replaced chest")
                            self.deff -= self.chest[0].armor
                            self.luck -= self.chest[0].luck
                            self.stamina -= self.chest[0].stamina
                            self.iq -= self.chest[0].iq
                            self.agi -= self.chest[0].agi
                            self.chest.remove(self.chest[0])
                            self.chest.append(i)
                            self.inventory.remove(i)
                            self.deff += self.chest[0].armor
                            self.luck += self.chest[0].luck
                            self.stamina += self.chest[0].stamina
                            self.iq += self.chest[0].iq
                            self.agi += self.chest[0].agi
                            break
                        elif x == "no":
                            self.inventory.remove(i)
                            break

    def equipBoots(self):
        for i in self.inventory:
            x = type(i)
            if "Boots" in str(x):
                if len(self.boots) < 1:
                    for i in self.inventory:
                        x = type(i)
                        if "Boots" in str(x):
                            print("you equipped a set of boots")
                            print(i)
                            self.boots.append(i)
                            self.inventory.remove(i)
                            self.deff += self.boots[0].armor
                            self.luck += self.boots[0].luck
                            self.stamina += self.boots[0].stamina
                            self.iq += self.boots[0].iq
                            self.agi += self.boots[0].agi
                else:
                    print("you need to remove equipped boots first")
                    print(self.boots[0])
                    print("would you like to replace them")
                    print(i)
                    while True:
                        x = input("yes or no")
                        if x == "yes":
                            print("you replaced boots")
                            self.deff -= self.boots[0].armor
                            self.luck -= self.boots[0].luck
                            self.stamina -= self.boots[0].stamina
                            self.iq -= self.boots[0].iq
                            self.agi -= self.boots[0].agi
                            self.boots.remove(self.boots[0])
                            self.boots.append(i)
                            self.inventory.remove(i)
                            self.deff += self.boots[0].armor
                            self.luck += self.boots[0].luck
                            self.stamina += self.boots[0].stamina
                            self.iq += self.boots[0].iq
                            self.agi += self.boots[0].agi
                            break
                        elif x == "no":
                            self.inventory.remove(i)
                            break

    def equipLegs(self):
        for i in self.inventory:
            x = type(i)
            if "leg" in str(x):
                if len(self.legs) < 1:
                    for i in self.inventory:
                        x = type(i)
                        if "Legs" in str(x):
                            print("you equipped a set of leg armor")
                            print(i)
                            self.legs.append(i)
                            self.inventory.remove(i)
                            self.deff += self.legs[0].armor
                            self.luck += self.legs[0].luck
                            self.stamina += self.legs[0].stamina
                            self.iq += self.legs[0].iq
                            self.agi += self.legs[0].agi
                else:
                    print("you need to remove equipped legs first")
                    print(self.legs[0])
                    print("would you like to replace them")
                    print(i)
                    while True:
                        x = input("yes or no")
                        if x == "yes":
                            print("you replaced legs")
                            self.deff -= self.legs[0].armor
                            self.luck -= self.legs[0].luck
                            self.stamina -= self.legs[0].stamina
                            self.iq -= self.legs[0].iq
                            self.agi -= self.legs[0].agi
                            self.legs.remove(self.legs[0])
                            self.legs.append(i)
                            self.inventory.remove(i)
                            self.deff += self.legs[0].armor
                            self.luck += self.legs[0].luck
                            self.stamina += self.legs[0].stamina
                            self.iq += self.legs[0].iq
                            self.agi += self.legs[0].agi
                            break
                        elif x == "no":
                            self.inventory.remove(i)
                            break
    def equipAll(self):
        self.equipBoots()
        self.equipChest()
        self.equipGloves()
        self.equipHead()
        self.equipLegs()
        self.equipWeapon()


    def useMpPotion(self):
        for i in self.inventory:
            if i == " mana potion":
                self.currMana = self.maxMana
                self.inventory.remove(i)
                return
    def useHpPotion(self):
        for i in self.inventory:
            if i == "health potion":
                self.currHealth = self.maxHealth
                self.inventory.remove(i)
                return

    def equipWeapon(self):
        for i in self.inventory:
            x = type(i)
            if ("Sword" in str(x) or "Axe" in str(x) or "Staff" in str(x)):
                while True:
                    x = input("would you like to equip the weapon in your right or left hand")
                    if x == "right":
                        if len(self.rightHand) < 1:
                            print("you equipped a weapon in your right hand")
                            print(i)
                            self.rightHand.append(i)
                            self.inventory.remove(i)
                            self.atk += self.rightHand[0].damage
                            self.luck += self.rightHand[0].luck
                            self.stamina += self.rightHand[0].stamina
                            self.iq += self.rightHand[0].iq
                            self.agi += self.rightHand[0].agi
                            break
                        else:
                            print("You already have a weapon in that hand")
                            print(self.rightHand[0])
                            print("would you like to replace that hand")
                            print(i)
                            while True:
                                x = input("Yes or no")
                                if x == "yes":
                                    print("You replaced the weapon")
                                    self.atk += self.rightHand[0].damage
                                    self.luck += self.rightHand[0].luck
                                    self.stamina += self.rightHand[0].stamina
                                    self.iq += self.rightHand[0].iq
                                    self.agi += self.rightHand[0].agi
                                    self.rightHand.remove(self.rightHand[0])
                                    self.rightHand.append(i)
                                    self.inventory.remove(i)
                                    self.atk += self.rightHand[0].damage
                                    self.luck += self.rightHand[0].luck
                                    self.stamina += self.rightHand[0].stamina
                                    self.iq += self.rightHand[0].iq
                                    self.agi += self.rightHand[0].agi
                                    break
                                if x == "no":
                                    self.inventory.remove(i)
                                    break

                    elif x == "left":
                        if len(self.leftHand) < 1:
                            print("you equipped a weapon in your right hand")
                            print(i)
                            self.leftHand.append(i)
                            self.inventory.remove(i)
                            self.atk += self.leftHand[0].damage
                            self.luck += self.leftHand[0].luck
                            self.stamina += self.leftHand[0].stamina
                            self.iq += self.leftHand[0].iq
                            self.agi += self.leftHand[0].agi
                            break
                        else:
                            print("You already have a weapon in that hand")
                            print(self.leftHand[0])
                            print("would you like to replace that hand")
                            print(i)
                            while True:
                                x = input("Yes or no")
                                if x == "yes":
                                    print("You replaced the weapon")
                                    self.atk += self.leftHand[0].damage
                                    self.luck += self.leftHand[0].luck
                                    self.stamina += self.leftHand[0].stamina
                                    self.iq += self.leftHand[0].iq
                                    self.agi += self.leftHand[0].agi
                                    self.leftHand.remove(self.leftHand[0])
                                    self.leftHand.append(i)
                                    self.inventory.remove(i)
                                    self.atk += self.leftHand[0].damage
                                    self.luck += self.leftHand[0].luck
                                    self.stamina += self.leftHand[0].stamina
                                    self.iq += self.leftHand[0].iq
                                    self.agi += self.leftHand[0].agi
                                    break
                                if x == "no":
                                    self.inventory.remove(i)
                                    break

                    else:
                        print("not an option")

    def attack(self):
        roll = random.randint(1,6)
        if roll == 1:
            print(self.name," Missed")
            return 0
        roll = random.randint(1, 12)
        if self.playerClass == "Warrior":
            for i in range(len(self.atklist)):
                print(i + 1, self.atk[i])
            while True:
                x = input("what attack will you use 1, 2, 3, or 4 to use a health potion")
                if x == "1":
                    attk = ((self.atk + self.stamina)*roll)*.1
                    break
                elif x == "2":
                    attk = ((self.atk + self.stamina) * roll) * .2
                    self.stamina -= 10


                    break
                elif x  == "3":
                    attk = ((self.atk + self.stamina) * roll) * .3
                    self.stamina -= 20
                    break
                elif x == "4":
                    self.useHpPotion()
                    atkk = 0
                    break
                else:
                    print("not and option")
        if self.playerClass == "Mage":
            for i in range(len(self.atklist)):
                print (i + 1, self.atklist[i])
            while True:
                x = input("what attack would you like to use 1, 2, 3, 4 for health potion and 5 for mana potion  ")
                if x == "1":
                    atkk = ((self.atk + self.iq)*roll)*.1
                    self.iq -= 5
                    break
                elif x == "2":
                    atkk = ((self.atk + self.iq) * roll) * .3
                    self.iq -= 10
                    break
                elif x == "3":
                    atkk = ((self.atk + self.iq) * roll) * .5
                    self.iq -= 30
                    break
                elif x == "4":
                    self.useHpPotion()
                    atkk = 0
                    break
                elif x == "5":
                    self.useMpPotion()
                    atkk = 0
                    break
                else:
                    print("sorry can't do that")
        if self.playerClass == "Hunter":
            for i in range(len(self.atklist)):
                print (i + 1, self.atklist[i])
            while True:
                x = input("what attack would you like to use 1, 2, 3, 4 for health potion and 5 for mana potion  ")
                if x == "1":
                    atkk = ((self.atk + self.agi)*roll)*.1
                    self.agi -= 5
                    break
                elif x == "2":
                    atkk = ((self.atk + self.agi) * roll) * .3
                    self.agi -= 10
                    break
                elif x == "3":
                    atkk = ((self.atk + self.agi) * roll) * .5
                    self.agi -= 30
                    break
                elif x == "4":
                    self.useHpPotion()
                    atkk = 0
                    break
                elif x == "5":
                    self.useMpPotion()
                    atkk = 0
                    break
                else:
                    print("sorry can't do that")
        if self.playerClass == "Dog":
            for i in range(len(self.atklist)):
                print (i + 1, self.atklist[i])
            while True:
                x = input("what attack would you like to use 1, 2, 3, 4 for health potion and 5 for mana potion  ")
                if x == "1":
                    atkk = ((self.atk + self.iq) * roll) * .1
                    self.luck += 5
                    break
                elif x == "2":
                    atkk = ((self.atk + self.iq) * roll) * .3
                    self.agi += 10
                    break
                elif x == "3":
                    atkk = ((self.atk + self.iq) * roll) * .5
                    self.atk += 30
                    break
                elif x == "4":
                    self.useHpPotion()
                    atkk = 0
                    break
                elif x == "5":
                    self.useMpPotion()
                    atkk = 0
                    break
                else:
                    print("sorry can't do that")
        if self.playerClass == "Karen":
            for i in range(len(self.atklist)):
                print (i + 1, self.atklist[i])
            while True:
                x = input("what attack would you like to use 1, 2, 3, 4 for health potion and 5 for mana potion  ")
                if x == "1":
                    atkk = ((self.atk + self.iq) * roll) * .1
                    self.iq -= 0
                    break
                elif x == "2":
                    atkk = ((self.atk + self.iq) * roll) * .3
                    self.iq -= 1
                    break
                elif x == "3":
                    atkk = ((self.atk + self.iq) * roll) * .5
                    self.iq -= 3
                    break
                elif x == "4":
                    self.useHpPotion()
                    atkk = 0
                    break
                elif x == "5":
                    self.useMpPotion()
                    atkk = 0
                    break
                elif x =="oof":
                    atkk = ((self.atk +self.iq)* roll)*1000000000000000000000000000000000000000*314
                    break
                else:
                    print("sorry can't do that")




        crit = 20
        if self.luck > 150:
            crit = 15
        roll = random.randint(1, crit)
        if roll == 14:
            attk = attk*3
        print(self.name, "did", attk, "damage")
        return attk

    def defend(self, damage):
        roll = random.randint(1,20)
        if roll == 20:
            print("Blocked")
            dmg = 0
        roll = random.randint(1, 6)
        if self.playerClass == "Warrior":
            block = ((self.deff + self.stamina) * roll) * .01
        elif self.playerClass == "Mage":
            block = ((self.deff + self.iq) * roll) * .01
        elif self.playerClass == "Hunter":
            block = ((self.deff + self.agi) * roll) * .01
        elif self.playerClass == "Dog":
            block = ((self.deff + self.stamina) * roll) * .01
        elif self.playerClass == "Karen":
            block = ((self.deff + self.stamina) * roll) * .01
        else:
            block = ((self.deff + self.iq) * roll) * .01
        print(self.name, "blocked", block, "damage")
        dmgdelt = dmg - block
        if dmgdelt >= 0:
            self.currHealth = self.currHealth-dmgdelt
        if self.currHealth <= 0:
            self.isAlive = False

    def unequipall(self):
        try:
            self.addToInv(self.Helm.pop(0))
            self.addToInv(self.Chest.pop(0))
            self.addToInv(self.Legs.pop(0))
            self.addToInv(self.Boots.pop(0))
            self.addToInv(self.Gloves.pop(0))
            self.addToInv(self.righHand.pop(0))
            self.addToInv(self.leftHand.pop(0))
        except:
            pass







