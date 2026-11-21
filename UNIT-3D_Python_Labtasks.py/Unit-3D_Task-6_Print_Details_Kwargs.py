# Function to print key-value pairs using **kwargs
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

# Function call
print_details(name="Krishna", age=26, city="Guntur")
