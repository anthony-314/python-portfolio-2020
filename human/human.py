import datetime
import time
import random

class Person():
    def __init__(self,name,last,age,haircolor,eyecolor):
        self.firstName = name
        self.lastName = last
        self.bday= datetime.datetime.now()
        self.lastbday = self.bday
        self.gen = ""
        self.height = 0
        self.body = 0
        self.age = 0
        self.weight = 0
        self.age = age
        self.strength = 0
        self.speed = 0
        self.hairColor = haircolor
        self.eyeColor = eyecolor
        self.race = ""
        self.voice = 0
        self.Iq = 0




    def intro(self):
        print("Hello my name is "+ self.firstName + " "+ self.lastName+"/n I have "+ self.hairColor +" Hair and " + self.eyeColor+ " Eyes and i am "+ str(self.age) +" years old")

    def aging(self):
        ctime = datetime.datetime.now().time()
        delta = datetime.timedelta(minutes=1)
        checktime = self.lastbday+delta
        if ctime >= checktime:
            self.age=+1
            self.lastbday = ctime
    def age2(self):
        self.age+=1
    def eat(self):
        print("Your fate will now be decieded")
        choice =["fat",'nothing','bigmac','carrot']
        x = random.randint(choice)
        print(self.weight)
        while True:
            if x=='carrot':
                self.weight += 1
            elif x == "fat":
                self.weight += 30
            elif x=="nothing":
                self.weight -= 10
            elif x =="bigmac":
                self.weight -= 5
            else:
                self.weight


bob = Person("bob","ross",98,'grey', 'blue')
bob.intro()
tim = Person("Tim","Johnson",75,"white","green")
tim.intro()
jack = Person("Jack","Nelson",45,"brown","brown")
jack.intro()
tom = Person("Tom","Seal",69,"blue","blue")
tom.intro()
sam = Person("sam","tensel",12,"green","white")
sam.intro()
gand = Person("Gandalf","grey",712,"white","grey")

#while True:
   # time.sleep(1)
   # bob.age2()
   # bob.intro()
bob.eat()