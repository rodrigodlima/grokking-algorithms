# This is an example of quicksort for sorting. When an array
# has only 1 element or zero elements, it doesn't need to be sorted

def quicksort(array):
    if len(array) < 2:
        return array
    

print(quicksort([3]))