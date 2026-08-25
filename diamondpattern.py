rows = int(input("Enter the number of rows : "))

if rows % 2 == 0:
    middle = rows // 2
else:
    middle = rows // 2 + 1

spaces = middle - 1

for i in range(1, middle + 1):

    for j in range(spaces):
        print(" ", end="")

    spaces -= 1

    num = 1

    for j in range(2 * i - 1):
        print(num, end="")
        num += 1

    print()

spaces = 1

for i in range(1, middle):

    for j in range(spaces):
        print(" ", end="")

    spaces += 1

    num = 1

    for j in range(1, 2*(middle - i)):
        print(num, end="")
        num += 1

    print()
    