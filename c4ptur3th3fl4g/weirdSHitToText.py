import random
import string


def printSolution(dictonary,weirdShit):
    for letter in weirdShit:
        print("".join(dictionary[letter]),end="")
    print()

def buildDictionary(letterSet,dictionary,alphabet):
    dict = dictionary
    for letter in letterSet:
        randomLetter = random.sample(alphabet,1)
        dict[letter] = randomLetter
        alphabet = alphabet.replace("".join(randomLetter),"")
    return dict
    
weirdShit = "fe `_` ``e bh ``d ba `_h hf `_f `_` ba ``e `_c `_d ``d ba hf ba hg `_d ``e ba ``e ``c `_d hh `_f `_d `_` ``c ce ce ce"
weirdShit = weirdShit.split(" ")
letterSet = set(weirdShit)
letterSet.remove("ce")
letterSet.remove("ba")
#letterSet.remove("hf")
#letterSet.remove("fe")
#letterSet.remove("hg")
#letterSet.remove("`_d")
#letterSet.remove("``e")
alphabet = string.ascii_lowercase
#print(len(letterSet))
#print("the letters are: ",letterSet)
#print("the alphabet is: ",letters)
dictionary = {}
dictionary = buildDictionary(letterSet,dictionary,alphabet)
dictionary["ce"] = "."
dictionary["ba"] = " "
#dictionary["hf"] = "a"
#dictionary["hg"] = "t"
#dictionary["`_d"] = "h"
#dictionary["``e"] = "e"
#dictionary["fe"] = "a"
for i in range(3000):
    printSolution(dictionary,weirdShit)
    dictionary = buildDictionary(letterSet,dictionary,alphabet)
