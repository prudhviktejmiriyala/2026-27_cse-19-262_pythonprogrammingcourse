from functools import reduce
numbers = [1, 2, 3, 4, 5, 6]
squares = list(map(lambda x: x ** 2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
total = reduce(lambda x, y: x + y, numbers)
print("Original List:", numbers)
print("Squares (map):", squares)
print("Even Numbers (filter):", evens)
print("Sum (reduce):", total)