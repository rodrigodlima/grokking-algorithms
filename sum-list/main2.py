#!/opt/homebrew/bin/python3

def sum_array(myList):
    total = 0
    for i in range(len(myList)):
        total = total + myList[i]
    return total


print(sum_array([1, 5, 6, 9]))
