# a python program to print numbers from 1 to N.
# Using For loop.
num = int(input("Enter a number: "))
for multiplier in range(1, 11):
    product = num * multiplier
    print(f"{num} x {multiplier} = {product}")
# Using While loop
num = int(input("Enter a number: "))
multiplier = 1
while multiplier <= 10:
    product = num * multiplier
    print(f"{num} x {multiplier} = {product}")
    multiplier = multiplier + 1