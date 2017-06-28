#Dictionary Excercises 
#Exercise: Letter Summary

def letter_summary():
    word = raw_input("Type in a word: ")
    letter_count = {}
    for stuff in word:
        for letter in stuff:
            if letter in letter_count:
                letter_count[letter] +=1
            else:
                letter_count[letter] = 1


#Haamza


    print letter_count

letter_summary()
