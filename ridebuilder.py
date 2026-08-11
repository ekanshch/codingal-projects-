
print("========================================")
print("     WELCOME TO THE RIDE BUILDER !!     ")
print("========================================")
print()

print("Step 1 : Pick your vehicle:-")
print("1. Bike")
print("2. Car")
print()

choice= int(input("Enter 1 or 2:"))
print()

if choice == 1:
    print("Step 2: Pick your Bike type")
    print(" 1.  Scooty")
    print(" 2. Mountain Bike")
    print()

    bike_type = int(input("Enter 1 or 2 :"))
    print()

    if bike_type == 1:
        print("You picked :- Scooty")
        print("Top speed  :- 40 km/h")
        print("Best for   :- City roads ")
    else:
        print("You picked :- Mountain Bike")
        print("Top Speed  :- 65 km/h ")
        print("Best for   :- Off road trails")

elif choice == 2:
    print("Step 2 : Pick your car type")
    print(" 1. Sedan")
    print(" 2. SUV")
    print()

    car_type = int(input("Enter 1 or 2 :"))

    if car_type == 1:
        print("You picked : Sedan")
        print("Seats      : 5 passengers")
        print("Best for   : Family Trips ")
    else:
        print("You picked : SUV")
        print("Seats      : 7 passengers")
        print("Best for   : Off-road adventures")

else:
    print("This is not a valid choice.")
    print("Enter 1 for bike or 2 for car.")