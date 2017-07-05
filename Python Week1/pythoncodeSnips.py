#1 to 10
# count = 1

# while count <= 10:
#     print count
#     count = count + 1

# n to m
# start = int(raw_input("start number: "))
# end = int(raw_input("end number? "))


# while start <= end:
#     print start
#     start = start +1

#odd numbers
# count = 1

# while count <=10:
#     if count % 2 != 0:
#         print count
#     count = count + 1

#How many coins
# coins = 0

# print ("your have %d coins.") % coins

# cond = True
# while cond:
#     coinQ = raw_input("do you want more coins? ")
#     coinA = coinQ
#     if coinA == "yes":
#         coins = coins + 1
#         print ("you have %d coins.") % coins
#     else:
#         cond = False
#         print("bye")

#print a sqaure
# size = 5
# i = 0
# while i <= size:
#     print ('*' * size)
#     i = i + 1 

#Print a Square II
# size = int(raw_input("how big is the square? " ))
# i = 0
# while i <= size:
#     print ("*" * size)
#     i = i + 1

#print a box
# width = int(raw_input("what is the width? "))
# height = int(raw_input("height? "))
# i = 0
# innerW = width - 2
# print("*" * width)
# while i < (height - 2) :
#     print ("*" + (innerW * " ") + "*")
#     i = i +1 
# print ("*" * width)

#print triangle

#    *    
#   ***
#  *****
# *******

# space = 3
# starC = 1
# while starC <= 7:
#     print ((" " * space) + ("*" * starC))
#     space = space - 1
#     starC = starC + 2

#print a Triangle 2 
height = int(raw_input("Give Height: "))
space = (height * 2)
starC = 1
while starC <= height:
    print ((" " * space) + ("*" * starC))
    space = space - 1
    starC = starC + 2


#multiplication table

# integer = 1
# multip = 1
# while integer <= 10:
#         statement = ("%d times %d equals") % (integer, multip)
#         total = integer * multip
#         print statement, total
#         multip = multip + 1
#         if multip > 10:
#                 multip = 1
#                 integer = integer + 1
        
#Print a Banner
# statement = raw_input("wright a statememt: ")
# length = len(statement) + 4
# print ("*" * length)
# print ("*" + " " + statement + " " + "*")
# print ("*" * length)

#triangle numbers
# triN = 1
# triC = 1
# while triN <= 100:
#     triC = triN * (triN + 1)/2
#     print triN, "is equal to ", triC
#     triN = triN + 1

#find factors of given number
# number = int(raw_input("What is your number: "))
# i = 1
# check = number % i
# while i <= number:
#     if number % i == 0:
#         print i
#     i = i + 1
        
    
#blastoff
# import time
# timer = (raw_input("Set count down timer: "))
# i = int(timer) 
# if i > 20:
#     print ("timer to high!")
# while i <= 20 and i > -1:
#     if i >= 0:
#         print i
#     i = i - 1
# if i < 0:
#     time.sleep(2)
#     print ("lift off!!!!!")

#Guess a number
import random
# secretNumber = random.randint(1, 10)
# limit = 5
# cond = True
# tryAgain = False
# while cond:
#     guess = int(raw_input("guess the number: "))
#     if guess == secretNumber:
#         print ('Hooray')
#         cond = False
#         tryAgain = True
#     else:
#         if guess > secretNumber:
#             print guess, 'Try again - number is too high'
#             limit = limit - 1
#             print 'lives left: ', limit
#         if guess < secretNumber:
#             print guess, 'Try again - number is too low'
#             limit = limit - 1
#             print 'lives left:', limit
#     if limit <= 0:
#         print('GAME OVER')
#         cond = False
#         tryAgain = True
#         while tryAgain:
#             again = (raw_input("play again? "))
#             if again == "yes":
#                 tryAgain = False
#                 cond = True
#                 limit = 5
#             if again == "no":
#                 print ('Bye')



