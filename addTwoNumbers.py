# This program adds two numbers and prints the result.
def add_two_numbers(a, b):
    return a + b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = add_two_numbers(num1, num2)

print(f"The sum of {num1} and {num2} is {result}")