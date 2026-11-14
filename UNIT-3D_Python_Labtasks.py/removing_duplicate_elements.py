n = int(input("Enter the number of elements: "))
numbers = []

for i in range(n):
    element = int(input("Enter element: "))
    numbers.append(element)
unique_list = []

for item in numbers:
    if item not in unique_list:
        unique_list.append(item)
print("Original List:", numbers)
print("List after removing duplicates:", unique_list)