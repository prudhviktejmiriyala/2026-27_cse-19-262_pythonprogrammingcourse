# Function to calculate Simple Interest
def simple_interest(principal, time, rate=5):
    si = (principal * time * rate) / 100
    return si

# Using default rate (5%)
interest1 = simple_interest(10000, 2)
print("Simple Interest with default rate:", interest1)

# Using an explicit rate (8%)
interest2 = simple_interest(10000, 2, 8)
print("Simple Interest with explicit rate:", interest2)