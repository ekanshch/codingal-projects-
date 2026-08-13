print("-"* 32)
print("    WELCOME TO THEME PARK !!    ")
print("-"* 32)
print()

#Name of the user
name = input("Enter your name :")
print()
print()
print(f"   WELCOME {name} !")

print()
age_user = int(input("Enter your age :"))
    
if age_user <= 13:
    print("SELECTED AGE GROUP: KIDS")
    print("Based on your age groups, you are allowed in these rides:")
    print()
    print("  1. Merry go round")
    print("  2. Mini train")
    selected_ride = int(input("Enter 1 or 2 :"))
    print()
    if selected_ride == 1:
        print("You have selected the Merry go round ride.")
        print()
        print("RIDE NAME   : MERRY - GO - ROUND")
        print("THRILL LEVEL: MEDIUM")
        print("WAITING TIME: 30 minutes")
    elif selected_ride == 2:
        print("You have selected the mini train ride.")
        print()
        print("RIDE NAME     : MINI TRAIN")
        print("THRILL LEVEL  : EASY")
        print("WAITING TIME  : 15 minutes")
    else:
        print("Invalid input. Enter 1 for Merry-go-round and 2 for mini train.")

else:
    print("SELECTED AGE GROUP: ADULTS")
    print("Based on your age groups, you are allowed in these rides:")
    print()
    print("  1. Roller coaster")
    print("  2. Giant wheel")
    selected_ride = int(input("Enter 1 or 2 :"))
    print()
    if selected_ride == 1:
        print("You have selected the roller coaster.")
        print()
        print("RIDE NAME          : ROLLER COASTER")
        print("THRILL LEVEL       : HARD")
        print("WAITING TIME       : 45 minutes")
        print("HEIGHT REQUIREMENT : 5 feet 2 inches ")

    elif selected_ride == 2:
        print("You have selected the giant wheel.")
        print()
        print("RIDE NAME          : GIANT WHEEL")
        print("THRILL LEVEL       : HARD")
        print("WAITING TIME       : 1 hour")
        print("HEIGHT REQUIREMENT : 5 feet")

    else: 
        print("Invalid input. Enter 1 for roller coaster and 2 for giant wheel.")


