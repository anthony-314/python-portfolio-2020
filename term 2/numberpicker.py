import random
import sys
print("Welcome the computer is going to guess your number")

minrange =int(input("what number do you want to start with?"))
mxrange = int(input("what do number do you want to go to?"))
num = int(input("now pick a number between your previous numbers"))

randnum = random.randint(minrange,mxrange)

trys = 0
maxTrys = 3
trys += 1
while num != randnum and trys != maxTrys:
    if num > randnum:
        
    else:
        
    num = testing_guess(rmin,rmax)
    trys += 1
