def search(arr, item):
    for i in range(len(arr)):
        if arr[i] == item:
            return i


my_list = [0, 2, 5, 9, 4]
print(search(my_list, 9))
