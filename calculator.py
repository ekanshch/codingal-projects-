# we will create a calculator 
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error  : A number cannot be divided by zero. Try using a different number."
    return x / y
def define_menu():
       print("\n\n")
       print("-" * 40)
       print("                    CALCULATOR                    ")
       print("-" * 40)
       print("Welcome to my calculator!")
       print("1.  ADDITION")
       print("2.  SUBTRACTION")
       print("3.  MULTIPLICATION") 
       print("4.  DIVISION")
       print("5.  EXIT")
       print("-" * 40)




while True:
    print(define_menu())
    choice = input("Enter your choice (1-5): ")
    
    if choice == "5":
        print("Thank you for using the calculator.  ")
        print("Have a great day ahead!!")
        break

    if choice in ("1", "2", "3", "4"):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if choice == "1":
            print(f"{num1} + {num2} = {add(num1, num2)}")

        elif choice == "2":
            print(f"{num1} - {num2} = {subtract(num1, num2)}")

        elif choice == "3":
            print(f"{num1} * {num2} = {multiply(num1, num2)}")

        elif choice == "4":
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")

    else:
        print("Invalid Input. Please enter a number between 1 and 5.")
        print("/n Press enter to continue.")

