#a python program to find the factorial of a number using for loop
number = int(input("Enter a number: "))
factorial = 1
for value in range(1, number + 1):
    factorial = factorial * value
print(f"Factorial of {number} is {factorial}")