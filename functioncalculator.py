def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

print("========Welcome to the Function Calculator!========")
print("You can perform the following operations:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("Or you can type 'exit' to quit the calculator.")

while True:
    try:
        operation = input("Enter the operation (add, subtract, multiply, divide) (or type 'exit'): ")
        if operation.lower() == 'exit':
            print()
            print()
            print("Exiting the calculator. Goodbye!")
            break

    except ValueError:
        print()
        print("Invalid input. Please enter a valid operation or type 'exit' to quit.")
        continue


    
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for the numbers.")
        continue    

      
    if operation.lower() == 'add':
        result = add(num1, num2)
        print()
        print(f"The result of addition is: {result}")
    elif operation.lower() == 'subtract':
        result = subtract(num1, num2)
        print()
        print(f"The result of subtraction is: {result}")
    elif operation.lower() == 'multiply':
        result = multiply(num1, num2)
        print()
        print(f"The result of multiplication is: {result}")
    elif operation.lower() == 'divide':
        result = divide(num1, num2)
        print()
        print(f"The result of division is: {result}")
    else:
        print("Invalid operation. Please choose from add, subtract, multiply, divide,"
               " or type 'exit' to quit.")
