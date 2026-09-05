try:
    num1, num2 = eval(input("Enter two numbers, seperated by a comma :-"))
    result = num1 / num2
    print(f"The result is {result}.")

except ZeroDivisionError:
    print("Division by zero is undefined. Please enter a non-zero denominator.")

except SyntaxError:
    print("The comma is missing. Please enter two numbers separated by a comma like this: 5, 2")

except:
    print("Wrong input.")

else:
    print("No exceptions.")

finally:
    print("This will execute no matter what.")
    