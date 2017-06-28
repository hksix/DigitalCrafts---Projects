# #reverse a String 

def reverseWord():
    #print word[::-1]
    word = obtainWord()
    rev_str = ""
    for i in word:
        rev_str = i + rev_str
    print rev_str

def obtainWord():
    wordU = str(raw_input("Type in a word: "))
    return wordU

reverseWord()