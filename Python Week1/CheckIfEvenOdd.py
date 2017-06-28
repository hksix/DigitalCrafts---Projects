#Check if input number is even or odd and if it is divisible by 4
number = input("what is your number: ")
number = int(number)
evenCheck = number 
if (evenCheck % 2) == 0 and (evenCheck % 4 == 0):
    print ("your number is an even number and divisible by 4")
elif (evenCheck % 2) == 0:
    print ("your number is even")
else:
    print ("your number is odd")