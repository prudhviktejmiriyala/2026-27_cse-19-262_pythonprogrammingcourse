n = int(input("Enter the number of values: "))
largest = float(input("Enter number 1: "))
for i in range(2, n + 1):
    num = float(input("Enter number {}: ".format(i)))

    if num > largest:
        largest = num

print("Largest number =", largest)