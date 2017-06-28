# #Capitalize a string

def capitalizeIt():
    word = obtainWord()
    firstLetter = word[0]
    restofName = word[1:]
    print firstLetter.upper() + restofName
    

def obtainWord():
    word_user = str(raw_input("type in a word: "))
    return word_user

capitalizeIt()


# Chris' code
# text = raw_input("Give me a string, please: ")
# print text[0].upper() + text[1:]