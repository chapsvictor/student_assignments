'''I used function to write the first 10 range numbers of fibonacci'''
def fibonacci(n):
    fib = [0, 1]  # Initialize the Fibonacci sequence with the first two numbers
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])  # Calculate the next Fibonacci number
    return fib

# Calculate the first 10 Fibonacci numbers
fibonacci_numbers = fibonacci(10)

# Print the Fibonacci numbers
for num in fibonacci_numbers:
    print(num)