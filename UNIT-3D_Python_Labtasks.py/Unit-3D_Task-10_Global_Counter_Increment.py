counter = 0
def increment_counter():
    global counter
    counter += 1
    print("Counter value:", counter)

# Function calls
increment_counter()
increment_counter()
increment_counter()