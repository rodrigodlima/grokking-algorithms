
def calc_factorial(num): 
    if num == 0 or num == 1:
        return 1
    else:
        num = num * calc_factorial(num - 1)
        return num


print(calc_factorial(5))
