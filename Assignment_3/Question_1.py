def basic_operations(a, b):
    print(f"Addition: {a + b}")
    print(f"Subtraction: {a - b}")
    print(f"Multiplication: {a * b}")
    if b != 0:
        print(f"Division: {a / b}")
    else:
        print("Division: Error (division by zero)")

# Taking input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
basic_operations(num1, num2)
