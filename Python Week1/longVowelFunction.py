#long long vowels
# word = "Good"
# vowels = ["a", "e", "i", "o", "u"]
# vowel_count = 0
# for i in word:
#     if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
#         vowel_count = vowel_count + 1
#         if vowel_count >= 2 and vowel_count != 1:
#             print word.replace(i, i+i+i+i,1)
#         else:
#             print("not enough vowels")
# word = raw_input("type in word: ")
# word_array = list(word)
# vCheck = 0
# for v in word:
#     if v == 'a':
#         print v

word = "Good"
vowels = ["a", "e", "i", "o", "u"]
j = ""
store = []
final = ""
for i in word:
    counter = 0
    wordSave = ""
    for v in vowels:
        if i == v:
            # wordSave = 
            final = final + (v *2)
            break
        else:
            final = final + i
        counter = counter + 1
        
print final

