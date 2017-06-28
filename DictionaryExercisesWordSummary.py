#Dictionary Excercises 
#Exercise: Word Summary

def words_summary():
    Testwords = "to be or not to be "
    words_array = []
    words_seperated = ""
    words_dict = {}

    for stuff in Testwords:
        if stuff != " ":
            words_seperated += stuff
        else:
             words_array.append(words_seperated)  
             words_seperated = "" 

    for xstuff in words_array:
        if xstuff in words_dict:
            words_dict[xstuff] +=1
        else:
            words_dict[xstuff] = 1
    
    print words_dict
    print words_dict.values()
    
        
words_summary()