def fib(x):
    fibonnaci_number = [0,1]  
    for i in range(2, x):
        fibonnaci_number.append(fibonnaci_number[i - 1] + fibonnaci_number[i - 2])
    return fibonnaci_number


fib_ten_numbers = fib(10)
for numbers in fib_ten_numbers:
    print(numbers, end=", ")

"""this is a code description of how i calculated the first ten number of a fibonnaci sequence"""