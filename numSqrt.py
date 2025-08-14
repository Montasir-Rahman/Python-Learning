# This program calculates the square root of a number and prints the result.
def num_sqrt(n):
    return n ** 0.5 
    
num = float(input("Enter a number: "))
result = num_sqrt(num)

print(f"The square root of {num} is {result}")