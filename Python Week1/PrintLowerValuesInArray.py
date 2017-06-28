# Print lower values in the array based of user input value
myArray = []
myArray.extend([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
num = int(raw_input("Choose a number to see what is lower in the array: "))
new_list = []
for i in myArray:
    if i < num:
        new_list.append(i)
print new_list