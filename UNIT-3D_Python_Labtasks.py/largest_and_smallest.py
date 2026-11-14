n = int(input("Enter the number of elements: "))
numbers = []
for i in range(n):
    element = int(input("Enter element: "))
    numbers.append(element)
largest = max(numbers)
smallest = min(numbers)
print("List:", numbers)
print("Largest element:", largest)
print("Smallest element:", smallest)