
def obtainTextInput():
    text = str(raw_input("type in text: "))
    text = text.upper()
    return text

def leetTrans():
    uppercased_text = obtainTextInput()
    letters_t0_convert = ['A','E','G','I','O','S','T']
    numbers = [4,3,6,1,0,5,7]    
    translation = ""
    for words in uppercased_text:
        counter = 0
        wordSave = ""
        for letter in letters_t0_convert:
            if words == letter:
                wordSave = str(numbers[counter])
                break
            else:
                wordSave = words
            counter = counter + 1
        translation = translation + wordSave
    print translation           
            
leetTrans()



# for letter in uppercased_text:
#     # print letters_t0_convert.index(letter)
#     counter =  0
#     letter_to_add_to_translation = ""
#     for letter_to_convert in letters_t0_convert:
#         # print "looking at ", letter_to_convert
#         if letter == letter_to_convert:
#             # print "FOUND IT! %s" % letter
#             # print "want to replace with %s" %numbers[counter]
#             # translation = translation + str(numbers[counter])
#             letter_to_add_to_translation = str(numbers[counter])
#             break
#         else:
#             # print "just use", letter
#             # translation  =translation + letter
#             letter_to_add_to_translation = letter
#         counter = counter + 1
#     translation = translation + letter_to_add_to_translation
# print translation































