# today we will create a daily activity planner 
temprature = int(input("Enter today's tempreature in celcius :"))
if temprature > 20:
    activity = "indoor reading"
    print("It is cool today")
    print("Do", activity)
else:
    activity = "outdoor games"
    print("It is warm today.")
    print("Do", activity)

 
is_raining = input("Is it raining today? (yes/no): ")
 
if is_raining == "yes":
    print("Choose an indoor activity or carry an umbrella!")
 
# PART 5: Ask for the homework time
homework_time = int(input("Enter homework time in minutes: "))
 
if homework_time > 60:
    needs_break = "yes"
    print("You have a long homework session today.")
    print("Take a short break before your", activity)
else:
    needs_break = "no"
    print("Homework time is short today.")
    print("No long break needed before your", activity)

has_free_time = input("Do you have free time today? (yes/no): ")
 
if has_free_time == "yes":
    final_task = "hobby time"
    print("You have free time today.")
    print("Enjoy your", final_task)
else:
    final_task = "planning time"
    print("You do not have much free time today.")
    print("Use some time for", final_task)

# printing that the daily activity check is complete
 
print("/n/n")
print("Daily activity check complete!")

print("=======DAILY ACTIVITY PLANNER=======")
print("TEMPRATURE:", temprature)
print("ACTIVITY CHOSEN :", activity)
print("RAINING :", is_raining)
print("STUDY BREAK NEEDED:", needs_break)
print("FINAL TASK:", final_task)
print("====================================")