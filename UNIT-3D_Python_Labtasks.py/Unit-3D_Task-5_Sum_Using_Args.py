# Function using *args to find the sum of any number of values
def find_sum(*args):
    return sum(args)

# Function calls
print("Sum =", find_sum(10, 20, 30))
print("Sum =", find_sum(5, 15, 25, 35, 45))
print("Sum =", find_sum(100, 200))