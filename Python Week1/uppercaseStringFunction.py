# #Uppercase a String


def obtainWord():
    word_user = str(raw_input("Type in a word "))
    return word_user

def upperCaseIt():
    word = obtainWord()
    print word.upper()
 
upperCaseIt()