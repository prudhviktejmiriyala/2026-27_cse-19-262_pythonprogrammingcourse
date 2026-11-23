n = int(input("Enter the number of values: "))
total = 0
for i in range(1, n + 1):
    num = float(input("Enter number {}: ".format(i)))
    total += num

average = total / n

print("Sum =", total)
print("Average =", average)