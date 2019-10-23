user =input("what is your user name")
word1 =input('enter an adj')
word2 =input('enter a noun')
word3 =input('enter a noun')
word4 =input('enter a pronoun')
word5 =input('enter a place')
word6 =input('enter an adj')
word7 =input('enter a noun')



text = str.format("""Be kind to your "{}"-footed "{}"
For a duck may be somebody`s "{}",
Be kind to your "{}" in "{}"
Where the weather is always "{}"

You may think that this is the "{}"
Well it is.""",word1,word2,word3,word4,word5,word6,word7)

print("This is your mad-lib " +user)
print(text)
