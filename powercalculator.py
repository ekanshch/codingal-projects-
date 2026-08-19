print("====================================")
print("       POWER CALCULATOR")
print("====================================")

num = int(input("Enter the number: "))
power = int(input("Enter the power: "))

result = 1

print("\nCalculating the answer :-")

for i in range(power):
    result = result * num

print("------------------------------------")
print(num, "raised to the power", power, "is:", result)
print("------------------------------------")

print("Thank you for using the Power Calculator!")
print("====================================")