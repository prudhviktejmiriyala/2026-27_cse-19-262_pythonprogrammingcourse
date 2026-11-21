def display_student(**kwargs):
    print("Student Details:")
    
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Function call
display_student(
    name="Ravi",
    Mathematics=85,
    Science=90,
    English=88
)
