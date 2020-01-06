#Anthony Peraza
#guess my number game
#10/19
#different levels of difficulty
import random
import sys

rmin = 0
rmax = 10
maxTrys = 3 

def easy ():

    rmin = 1
    rmax = 11
    maxTrys = 3
    game(rmin, rmax, maxTrys)
def medium ():

    rmin = 1
    rmax = 50
    maxTrys = 5
    game(rmin, rmax, maxTrys)
def hard ():
  

    rmin = 1
    rmax = 100
    maxTrys = 8
    game(rmin, rmax, maxTrys)
def impossible ():

    rmin = 1
    rmax = 1000
    maxTrys = 1
    game(rmin, rmax, maxTrys)


def testing_guess (rmin,rmax):
    while True:
        guess = input("Pick a number between "+str(rmin) +' and ' +str(rmax)+"\n")
        if guess.isdigit():
            guess = int(guess)
            if guess <= rmax and guess >= rmin:
                return guess
            print("not a good value")
#set up program
def game(rmin, rmax, maxTrys):
    randnum = random.randint(rmin,rmax)


    trys = 0

    num =  testing_guess(rmin,rmax)
    trys += 1
    while num != randnum and trys != maxTrys:
        if num > randnum:
            print("guess lower")
        else:
            print("guess higher")
        num = testing_guess(rmin,rmax)
        trys += 1

    if num == randnum:
        print("winner")
    else:
        print("loser")
    print('nuber was',randnum)


def menu(rmin, rmax, maxTrys):
    while True:
        
        print("""
    press 1 for option
    press 2 for game
    press 3 to quit
    """)
        choice = input("")
        if choice == "1":
              
            print("easy = 0 , medium = 1, hard = 2 impossible = 3")
            diff = str(input("what level of difficutly do you want?"))
            if diff == "0":
                easy()
            elif diff == "1":
                medium()
            elif diff == "2":
                hard()
            elif diff == "3":
                impossible()

        if choice == "2":
            game(rmin, rmax, maxTrys)

        if choice == "3":
            sys.exit()
     

menu(rmin, rmax, maxTrys)








            
