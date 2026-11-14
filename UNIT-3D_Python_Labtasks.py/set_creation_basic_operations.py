set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print("Set 1 =", set1)
print("Set 2 =", set2)
print("\nUnion of Set 1 and Set 2:")
print(set1.union(set2))
print("\nIntersection of Set 1 and Set 2:")
print(set1.intersection(set2))
print("\nDifference (Set1 - Set2):")
print(set1.difference(set2))

print("\nDifference (Set2 - Set1):")
print(set2.difference(set1))