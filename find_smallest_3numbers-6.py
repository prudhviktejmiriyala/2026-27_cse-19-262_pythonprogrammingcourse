# A python program to find the smallest of three numbers using nested if.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Find the smallest using nested if statements
if num1 <= num2:
    if num1 <= num3:
        smallest = num1
    else:
        smallest = num3
else:
    if num2 <= num3:
        smallest = num2
    else:
        smallest = num3

print("The smallest number is:",smallest)