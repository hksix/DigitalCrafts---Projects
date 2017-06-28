# find the outlier

def find_outlier(array):
    evenArray = []
    oddArray = []
    lengthEven = []
    lengthOdd = []

    for i in array:
        if i % 2 == 0:
            evenArray.append(i)
            lengthEven = len(evenArray)
        if i % 2 != 0:
            oddArray.append(i)
            lengthOdd = len(oddArray)
    if lengthEven <= 1:
            print evenArray
    if lengthOdd <= 1:
            print oddArray

# array = [2, 4, 0, 100, 4, 11, 2602, 36]
array = [160, 3, 1719, 19, 11, 13, -21]
find_outlier(array)