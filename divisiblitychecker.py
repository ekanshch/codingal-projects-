print("Enter a number (Numerator):")
num1 = int(input())
print("Enter a number (Denominator):")
num2 = int(input())

if num1 % num2 == 0:
    print(num1, "is divisible by", num2)
else:
    print("\n", num1, "is not divisible by", num2)