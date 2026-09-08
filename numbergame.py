import random
playing = True
number = str(random.randint(1, 10))

print("I will generate a number between 1 and 10. You have to guess it.")
print("The game ends when you guess the number correctly.")

while playing:
    guess = input("Give me your best guess: \n")
    if number == guess:
        print("You win the game.")
        print("The number was: " + number)
        break

    else:
        print("You guessed wrong. Try again.")