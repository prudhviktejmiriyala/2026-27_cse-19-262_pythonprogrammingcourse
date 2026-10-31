#a python program to print the multiplication table of a number
# using for loop
num = int(input("Enter a number: "))
for multiplier in range(1, 11):
    product = num * multiplier
    print(f"{num} x {multiplier} = {product}")
# using while loop
num = int(input("Enter a number: "))
multiplier = 1
while multiplier <= 10:
    product = num * multiplier
    print(f"{num} x {multiplier} = {product}")
    multiplier = multiplier + 1