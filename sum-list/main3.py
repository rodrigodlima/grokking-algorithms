#!/opt/homebrew/bin/python3

def sum_list(myList):
    total = 0
    for i in range(len(myList)):
        total = total + myList[i]
    return total


print(sum_list([2, 5, 7, 9]))
