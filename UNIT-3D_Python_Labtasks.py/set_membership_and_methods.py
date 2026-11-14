numbers = {10, 20, 30, 40}

print("Original Set:", numbers)
print("\nMembership Testing:")
print("20 in set?", 20 in numbers)
print("50 in set?", 50 in numbers)
numbers.add(50)
print("\nAfter adding 50:", numbers)
numbers.remove(20)
print("After removing 20:", numbers)
numbers.discard(30)
print("After discarding 30:", numbers)