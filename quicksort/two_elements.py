def sort_array(myarray):
    i = 0
    if range(myarray[i]) > range(myarray[i+1]):
        value = myarray[i]
        return myarray[value, i]
    else:
        value = myarray[i+1]
        return myarray[value, i]


print(sort_array([1, 3]))