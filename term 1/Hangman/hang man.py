import random
HANGMAN = (
"""
 --------
 1      1
 1      
 1
 1
 1
 1
 1
 1
 1
 1
----------
""",
"""
 --------
 1      1
 1      O
 1
 1
 1
 1
 1
 1
 1
 1
----------
""",
"""
 --------
 1      1
 1      O
 1     -+- 
 1
 1
 1
 1
 1
 1
 1
----------
""",
"""
 --------
 1      1
 1      O
 1    /-+-\ 
 1
 1
 1
 1
 1
 1
 1
----------
""",
"""
 --------
 1      1
 1      O
 1    /-+-\ 
 1      1
 1       \<
 1
 1
 1
 1
 1
----------
""",
"""
 --------
 1      1
 1      O
 1    /-+-\ 
 1      1
 1    >/ \<
 1
 1
 1
 1
 1
----------
""",
"""
 --------
 1      1
 1      1
 1      O
 1    /-+-\ 
 1      1
 1    >/ \<
 1
 1
 1
 1
 1
----------
""",
"""
 --------
 1      1
 1      1
 1      O
 1      {
 1    /-+-\ 
 1      1
 1    >/ \<
 1
 1
 1
 1
 1
----------
""",
"""
YOU DIED""")

MAX_WRONG = len(HANGMAN)-1
WORD_BANK = ["OVERUSED", "CLAM", 'GUAM', 'TAFFETA', 'PYTHON']

word = random.choice(WORD_BANK)
so_far = "-" *len(word)

wrong = 0
used = []

print("welcome to hangman. Don't die:")

while wrong < MAX_WRONG and so_far != word:
    
    print(HANGMAN[wrong])
    print("\nYou've used the following letters:\n",used)
    print("\nSo far, the word is :\n", so_far)

    guess = input ("\n\nEnter your guess: ")
    guess = guess.upper()

    while guess in used:
        print("You've already guessed the letter", guess)
        guess = input("\n\nEnter your guess: ")
        guess = guess.upper()

    used.append(guess)
    if guess in word:
        print("\nYes!", guess, "is in the word!")
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
            so_far = new
    else:
        print("\nSorry,", guess, "isn't in the word.")
        wrong += 1
if wrong == MAX_wrong:
    print(HANGMAN[wrong])
    print("\nOH NO! where did your head go?")
else:
    print("\nYOU DID IT!")

print("\nThe word was", word)
input("\nPress the enter key to exit.")
        
    


