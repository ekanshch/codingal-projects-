a = int(input("Enter a value for a: "))
b = int(input("Enter a value for b: "))
c = int(input("Enter a value for c: "))

avg = (a + b + c) / 3
print("Average is:", avg)

if avg > a and avg > b and avg > c:
    print("%d is higher than %d, %d and %d" % (avg, a, b, c))

elif avg > a and avg > b:
    print("%d is higher than %d and %d" % (avg, a, b))
elif avg > a and avg > c:
    print("%d is higher than %d and %d" % (avg, a, c))
elif avg > b and avg > c:
    print("%d is higher than %d and %d" % (avg, b, c))
elif avg > a:
    print("%d is higher than %d" % (avg, a))
elif avg > b:
    print("%d is higher than %d" % (avg, b))
elif avg > c:
    print("%d is higher than %d" % (avg, c))
else: 
    print("Invalid Input.")
    