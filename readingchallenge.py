goal = int(input("Enter your reading goal (pages) :- "))

a = 0
day = 1
print("\n Reading challenge started !!")

while a < goal:
    print("\n Day ", day)

    pages = int(input("How many pages did you read today?"))

    a = a + pages
    print("Total Pages Read :", a)
    print("Pages remaining :", goal - a)
    day = day + 1

print("\n Congratulations!!")
print("You completed your reading challenge.")
print("Total pages read :", a)
print("Days taken:", day - 1)
