import random
class Player(object):
    def __init__(self,name):
        self.health = 100
        self.name = name
        self.isAlive = True

    def shoot(self, target):

        miss = random.randint(0,1)
        if miss == 1:
            print("miss")
        else:
            target.takedmg()

    def takedmg(self):
        dmg_zone = random.randint(0,2)
        if dmg_zone == 0:
            print("lost limb")
            self.health -= 10
        elif dmg_zone == 1:
            print("whole in stomach")
            self.health -= 50
        else:
            print("head shot")
            self.health -= 100

        if self.health <=0
            self.die()
    def die(self):
        print("you have died")
        self.isAlive = False
    def __str__(self):
        rep = self.name+" has "+str(self.health)+" health left "
        return rep


class Alien(Player):
    def __init__(self):
        super(Alien, self).__init__("Alien")
    def die(self):
        print(" The aliens head blows up showering the air with the life vapor showering down upon you")
        self.isAlive = False



def main():
    us = Player("Ant")
    us.die()
main()
