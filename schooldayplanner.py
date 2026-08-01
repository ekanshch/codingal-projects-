#today we will create a school day planner 
print("========SCHOOL DAY PLANNER=======/n")
print("Answer three quick questions and I will plan your day! /n/n")
day = input("What day is it today? (Monday to Sunday): ").strip().capitalize()
weather = input("What is the weather ? (sunny, rainy, cloudy, windy)").strip().lower()
homework = input("Is your homework done? (yes/no): ").strip().lower()

print("/n/n")
print(f"Your plan for the {day} is ready!!")
print(f"=====YOUR PLAN FOR {day} =====")
print("-" * 30)

if day in ("Saturday", "Sunday"):
    print("Day Type            : Weekend - Enjoy your free time!!")
elif day in ("Monday"):
    print("Day Type            : First day of the week - Pack your weekly planner. ")
elif day in ("Tuesday" , "Wednesday", "Thursday"):
    print("Day Type            : Regular school day - Stay focused and complete your tasks.")
elif day in ("Friday"):
    print("Day Type            : Last school day - Return library books today.")
else:
    print("Day Type            : Not recognised - Please check the spelling.")

if weather == "sunny" and homework == "yes":
    print("After school: Head to the park - great weather and your homework is done!")

if weather == "rainy" or weather == "cloudy" or weather == "windy":
    print("Weather Tip      : Carry an umbrella or wear a raincoat - It may get wet outside.")

if not (homework == "yes"):
    print("Homework      : Not done yet - Complete it before going out.")

if weather == "rainy" and not (homework == "yes"):
    print("Best plan   : Stay in and finish your homework, then watch your favourite show or read a book.")
elif weather == "sunny" and homework == "yes" and not(day in ("Saturday", "Sunday")):
    print("Best plan   : All set for a great school day!! - you are prepared")
elif day in ("Saturday", "Sunday") and weather == "sunny":
    print("Best plan   : Enjoy your weekend - go out and have fun in the sun!")
else:
    print("Best plan   :Take it one step at a time - YOU HAVE GOT THIS!!")

print("")
print("Plan complete! Have a great day ahead!!")
print("-" * 30)

