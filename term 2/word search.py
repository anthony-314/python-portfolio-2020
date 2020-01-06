import math
Word_Bank = ["function","syntax","list","append","pop","concatanate","timestamp",
     "strftime", 'modulus','import','error',"array","index","tuple","return",
          "range","pound", 'string', 'char', 'data']


QUESTIONS =[ "what do you call something that peforms something",
"What type of error do you get when your program doesn't run",
"What do you use to hold multiple values in a single variable so you can change it later",
"what would you use to add something to a list later in your code",
"what would you use to take someth out of your list later in your code",
"What is it called when you combine to variables",
"What do you call the short cuts for time type stuff",
"converts a tuple or struct_time representing a time as returned by gmtime() or localtime() to a string as specified by the format argument",
"what do you call the percent sign in python",
"how do you bring in python libraries",
"when you something doesn't work out in your code what is it most likely",
"what is a collection of items stored at contiguous memory locations",
"what function can you use to sort through lists",
"what is an unchageable list",
"how do you call back a function",
"the length or entire parameter of you list",
"what comments things out",
"what data type to you get from an input",
"*$%!&",
"what is information",]
ANSWERS =[(26,17,26,24),(7,6,7,11),(1,27,4,30),(12,17,12,22),(19,27,19,30),(6,29,16,29),(1,6,1,14),(13,9,20,16),(5,14,5,20),(17,17,17,22),(5,28,9,28),(24,12,28,16),(25,2,25,6),(23,25,27,29),(16,10,21,10),(15,11,15,15),(1,25,5,29),(17,2,22,7),(12,2,12,5),(1,17,1,20)]
PUZZLE = "APUYZIJIYWHIUVYYLPUCJAALWPYNOMARFERBLFYJPCOOWCSQMUUUSFIUSSMURMSSCMCDVAHHSKYZXTFHDPCHNXZJJUNAJIMXJJNFRAHFTBBWRYGEVRDMMKZXBZNFQRQFWGKRUJYOIJGIDMCKEVHOTXTAMMZBSULXJCKWLATKIFNOSPXUAPWHIPODGUYZQJRCJDTFCIRHBGITRAGZDIMQDNNANROHCDNPXGGFQTMCPUJYMBZGEQXTERTZCSCXSJNWZTKYWQVKAXTJIXSDBZOHAXATBONTSRETURNQRABEKZNYTVRWCIXBVTMZKLRVDCNTYKXALRCDQPAWIKIAPOFKTNLWAFIMSQMACAEGYAZUMWJTRAKAVSMKOKNQTDRRFUHSRDKWZWPWANMNIVVECDDXGNWIOPWAFAFRNTTVRKMGOPMQRUOWXMESSDMGGMCDHFARBHYUNDDIMXUBUISVFZVYHEBKWQYEKYMWDNPMUWQGKRNABYEEIMPORTTTSFSAYZAHEKLSECUMFPNAUOQFRCXJNKFUIKYNTCBNUFKUELIPLHTLHHGEKJSGHNFPDBAAMUSPSPPKFEIWHQXEXCFDBFBCGSRYPWUMVMXMDCMNHLIOZFPAUHVPMTBLWXLNCANERUNRQDBEHDNUPMDEULDILYIKVTUZAGONJESCIGQFFIQRRMSWZOXMCWBWNIXWYYPYLWXKEWVWSZXRSVJNQHFLPAWQJGDIOMFRZRJULEDUGLTLEBGRPPFOLXAWUAHOZIVROSHXJMEDVUEZJXAMLZUSICHGUWLDCJCQHFDBJSPFPDXJIGZIJNERRORAJMCUVLJHPSPNGDTLCSUANJSMDCONCATANATEDEOWUNBEGOEXHYDHOTAXHOHCGUNPVLWTPUPIDBRAJFZE"
ROWS = 30 
COLS= 30
words = []
quests = []
##def display_puzzle(x) :
##    minIndex = 0
##    maxIndex = 30
##    for i in range(30):
##        for letter in x[minIndex:maxIndex]:
##            print(letter, end=" ")
##        print()
##        minIndex = minIndex + 30
##        maxIndex = maxIndex + 30
def display_puzzle(puzzel,colums,rows):
    """displays Puzzel"""
    i = 0
    print("     1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30")
    
    for col in range(colums):
        if col < 9:
            line = str(col+1)+"  | "
        else:
            line = str(col+1)+" | "
         
        for row in range(rows):
            line += puzzel[i]+" | "
            i += 1
        print(line)
display_puzzle(PUZZLE,30,30)

def word():
    import random
    
    
    while True:
        red = random.randint(0,len(Word_Bank)-1)
        randWord = Word_Bank[red]
        randQuest = QUESTIONS[red]
        if (randWord in words) or (randQuest in quests):
            continue
        else:
            words.append(randWord)
            quests.append(randQuest)
            return randWord, randQuest

    for i in range(len(Word_Bank)-1):
        answer,question = word()
        print(answer)
        print(question)




