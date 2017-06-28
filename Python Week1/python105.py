# #python 105
# #String Exercises



#leetSpeak Question rewriting without replace
# paragraph = "this is a test for a paragraph for leet"
# leet = ""
# for i in paragraph:
#     if i == 'a':
#         paragraph = paragraph.replace('a','4')
#     if i == 'e':
#         paragraph = paragraph.replace('e','3')
#     if i == 'g':
#         paragraph = paragraph.replace('g','6')
#     if i == 'i':
#         paragraph = paragraph.replace('i','1')
#     if i == 'o':
#         paragraph = paragraph.replace('o','0')
#     if i == 's':
#         paragraph = paragraph.replace('s','5')
#     if i == 't':
#         paragraph = paragraph.replace('t','7')
    
# print paragraph


#Long-long Vowels
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
        
        

#sum the numbers
# numbers = [1, 2, 3, 4, 5, 6]
# # numbers = range(10)
# sum = 0
# for num in numbers:
#     sum = sum + num
# print sum

# #largest and smallest
# import random
# numbers = [(random.randint(1, 10)) for k in range(10)]
# numbers.sort()
# length = len(numbers)-1
# print numbers[0],"is the smallest number"
# print numbers[length]
    
# print max(numbers)
# print min(numbers)

#even numbers
# numbers = range(21)
# evenList = []
# for i in numbers:
#     if i % 2 == 0:
#         evenList.append(i)
# print evenList

#Positive numbers
# numbers = range(-10, 20)
# pList = []
# for i in numbers:
#     if i >=0:
#         print i 

#Positive numbers 2
# numbers = range(-10, 20)
# pList = []
# for i in numbers:
#     if i >=0:
#         pList.append(i)
# print pList 

#Multiply an List by factor
# numbers = range(10)
# factor = 3
# mList = []
# for i in numbers:
#     n = i * factor
#     mList.append(n)
# print mList

#Multiply Vectors
# vectorOne = [0, 1, 2]
# vectorTwo = [3, 4, 5]
# mVector = []
# j = 0
# for i in vectorOne:
#     mVector.append(i * vectorTwo[j])
#     j = j +1 
# print mVector

#Matrix Addition
# matrixOne = [[1, 2], [3, 4]]
# matrixTwo = [[2, 4], [3, 5]]
# matrixsum = []
# j = 0
# v = 0
# for i in matrixOne:
#     matrixsum.append(i + matrixTwo[[i][i]])
#         for j in matrixTwo:


# print matrixsum

# twoD1 = [[1, 2], 
#         [3, 4]]
# twoD2 = [[2, 4], 
#         [3, 5]]
# new_matrix = []
# i=0
# for row in twoD1:
#     new_row = []
#     j = 0
#     for value in row:
#         new_row.append(value + twoD2[i][j])
#         j += 1
#     new_matrix.append(new_row)
#     i += 1    
# print new_matrix