def sort_array(myarray):
    i = 0
    if myarray[i] > myarray[i+1]:
        return [myarray[i+1], myarray[i]]
    else:
        return [myarray[i], myarray[i+1]]


print(sort_array([3, 2]))