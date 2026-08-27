#today we are creating a number guessing game   
print("=========WELCOME!==========")
print("===TO THE NUMBER GUESSING GAME===")
print()
print("In this game you will try to guess a number (from 1 to 100) in just 3 chances")
print("After each guess we will tell you how close you are from the number by:-")
print()
print("🧊 ice cold :- very far from the number ")
print(" 🔥 hot     :- very close ")
print("🥶 cold     :- far from the number")
print("🌡️ warm     :- close to the number")
print()
print("You will have 3 hearts (❤️❤️❤️)")
print()


secret = 30
guessed = True
while guessed:
    first = int(input("Enter your first guess (1-100) : "))

    if first == 30:
        print("Your guess was correct!")
        print("Congratulations!!")
        break
    elif first <= 10:
        print("🥶 cold ")
        print("You are far from the number.")
        print("❤️❤️ hearts remaining!")

    elif first <= 20 and first >= 10:
        print("🌡️ warm")
        print("You are a little bit close ")
        print("❤️❤️ hearts remaining!")

    elif first >= 45  and first >= 100:
        print("🧊 ice cold")
        print("You are very far from the number ")
        print("❤️❤️ hearts remaining!")

    elif first >= 20 and first <= 30:
        print("🔥 hot")
        print("You are very close to the number ")
        print("❤️❤️ hearts remaining!")

    elif first >= 30 and first <= 45:
        print("🔥 hot")
        print("You are very close to the number ")
        print("❤️❤️ hearts remaining!") 

    else:
        print("Invalid input. try again.")
        continue

    second = int(input("Enter your second guess (1-100) : "))

    if second == 30:
        print("Your guess was correct!")
        print("Congratulations!!")
        break
    elif second <= 10:
        print("🥶 cold ")
        print("You are far from the number.")
        print("❤️ hearts remaining!")
    
    elif second <= 20 and second >= 10:
        print("🌡️ warm")
        print("You are a little bit close ")
        print("❤️ hearts remaining!")
    
    elif second >= 45  and second >= 100:
        print("🧊 ice cold")
        print("You are very far from the number ")
        print("❤️ hearts remaining!")
    
    elif second >= 20 and second <= 30:
        print("🔥 hot")
        print("You are very close to the number ")
        print("❤️ hearts remaining!")
    
    elif second >= 30 and second <= 45:
        print("🔥 hot")
        print("You are very close to the number ")
        print("❤️ hearts remaining!") 
    
    else:
        print("Invalid input. try again.")
        continue

    third = int(input("Enter your third guess (1-100) : "))

    if third == 30:
            print("Your guess was correct!")
            print("Congratulations!!")
            break
    elif third <= 10:
        print("🥶 cold ")
        print("You are far from the number.")
        print("0 hearts remaining!")
        
    elif third <= 20 and third >= 10:
        print("🌡️ warm")
        print("You are a little bit close ")
        print("0 hearts remaining!")
        
    elif third >= 45  and third >= 100:
        print("🧊 ice cold")
        print("You are very far from the number ")
        print("0 hearts remaining!")
        
    elif third >= 20 and third <= 30:
        print("🔥 hot")
        print("You are very close to the number ")
        print("0 hearts remaining!")
        
    elif third >= 30 and third <= 45:
        print("🔥 hot")
        print("You are very close to the number ")
        print("0 hearts remaining!") 
        
    else:
        print("Invalid input. try again.")
        continue

    break
        
