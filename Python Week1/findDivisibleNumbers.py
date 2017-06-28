# find all divisible numbers of user input and push to array
number = int(raw_input("choose a number to see what is divisible: "))
divsibleNum = list(range(2, number+1))
divisorList = []
for elem in divsibleNum:
    if number % elem == 0:
            divisorList.append(elem)
print (divisorList)