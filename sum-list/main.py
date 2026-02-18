#!/opt/homebrew/bin/python3

def sum_list(mylist):
    total = 0
    for i in range(len(mylist)):
        total = total + mylist[i]
    return total


print(sum_list([2, 3, 5]))
