import random

class Hero(object):
    raceList = ["Human","Elf","Dwarf", "K9"]
    classList = ["Warrior","Mage","Hunter","Dog","Karen"]
    def __init__(self):
        self.alive = True
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
        self.head = ""
        self.head = []
        self.chest = []
        self.legs=[]
        self.boots=[]
        self.gloves = []
        self.rightHand = []
        self.leftHand = []

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
            self.stamina = random.randint(8, 12)
            self.agi = random.randint(3, 4)
            self.iq = random.randint(15, 20)
            self.deff = random.randint(1 , 2)
            self.atk = random .randint(6, 12)
            self.luck = random.randint(10, 15)
        #if self.playerClass == "Hunter":


    def die (self,champ):
        self.alive = False
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






