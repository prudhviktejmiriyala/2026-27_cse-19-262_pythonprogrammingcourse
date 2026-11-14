tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)
result = tuple1 + tuple2
print("Concatenated Tuple:", result)
print("First three elements:", result[:3])
print("Last three elements:", result[3:])
print("Middle elements:", result[2:5])
a, b, c = tuple1
print("\nTuple Unpacking:")
print("a =", a)
print("b =", b)
print("c =", c)