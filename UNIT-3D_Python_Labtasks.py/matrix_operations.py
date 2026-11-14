rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
print("Enter elements of Matrix A:")
A = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    A.append(row)
print("Enter elements of Matrix B:")
B = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    A_row = row
    B.append(row)
addition = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j] + B[i][j])
    addition.append(row)
subtraction = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j] - B[i][j])
    subtraction.append(row)
multiplication = []
for i in range(rows):
    row = []
    for j in range(cols):
        total = 0
        for k in range(cols):
            total += A[i][k] * B[k][j]
        row.append(total)
    multiplication.append(row)
print("\nMatrix Addition:")
for row in addition:
    print(row)

print("\nMatrix Subtraction:")
for row in subtraction:
    print(row)

print("\nMatrix Multiplication:")
for row in multiplication:
    print(row)