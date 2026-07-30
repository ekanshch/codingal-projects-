print("WELCOME TO ADVENTURE PARK!!!!")
age = int(input("Enter your age :"))
height = int(input("Enter your height in cm :"))
heart_problem = input("Do you have any heart problem ??(yes/no) :")
vip_pass = input("Do you have a vip pass ? (yes/no) :")

if age >= 10 :
    if height >= 140:
        if heart_problem == "no":
            print("CONGRATULATIONS!!")
            print("You are allowed on the ride!")

            if vip_pass == "yes":
                print("You can skip the queue!")
            else:
                print("Please wait in regular queue.")

        else:
            print("Sorry!!")
            print("For your safety, You cannot take this ride.")

    else:
         print("Sorry!!")
         print("Your height must be 140cm tall or above.")

else:
     print("Sorry!!")
     print("You must be at least 10 yrs old.")
     
