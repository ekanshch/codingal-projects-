#we will create a holiday activity planner 
print("---------------------------------------")
print(" Welcome to Holiday Activity Planner !")
print("---------------------------------------")

print("Choose your holiday type :-")
print()
print(" 1. Beach ")
print(" 2. Mountains")

choice = int(input("Enter 1 or 2 :"))
print()

if choice == 1:
    print("Pick your beach activity :-")
    print()
    print(" 1. Swimming")
    print(" 2. Sandcastle Building")
    print()

    beach_activity = int(input("Enter 1 or 2 :"))

    if beach_activity == 1:
        print("You picked   : Swimming")
        print("Best time    : Morning")
        print("Remember     : Carry sunscreen and water ")

    elif beach_activity == 2:
        print(" You picked    : Sandcastle Building")
        print("Best time      : Evening ")
        print("Remember       : Carry a bucket and a spade")

    else:
        print("Invalid input. Please try again by choosing either 1 or 2.")

elif choice == 2:
    print("Pick your mountain activity :-")
    print()
    print(" 1. Hiking")
    print(" 2. Camping")

    mountain_activity = int(input("Enter 1 or 2 :"))

    print()

    if mountain_activity == 1:
        print(" You picked      : Hiking ")
        print(" Best for        : Exploring trails ")
        print(" Remember        : Wear comfortable shoes ")

    elif mountain_activity == 2:
        print("You picked      : Camping ")
        print("Best for        : Staying close to nature ")
        print("Remember        : To carry a tent and a flashlight ")

    else:
        print("This is not a valid choice.")
        print("Enter 1 or 2.")

else:
    print("This is not a valid choice.")
    print("Enter 1 for beach holiday and 2 for mountain holiday.")
