total_chores = 4
original_count = total_chores
print(f" You have {original_count} chores to finish today!! \n")

completed_count = 0
chore_num = 1

while chore_num <= total_chores:

    if chore_num == 1: next_chore = "Make your bed"
    elif chore_num == 2: next_chore = "Feed the pet"
    elif chore_num == 3: next_chore = "Take out the trash"
    else: next_chore = "Wash the dishes"

    answer = input(f"Have you finished: {next_chore}? (yes/no) :-")

    if answer == "yes":
        completed_count += 1
        chore_num += 1
        print("Great Job! Chore completed.")

    else:
        print("Okay. finish it and check again!")


    print("Chore remaining :", total_chores - completed_count)
    print()

print("===== ALL CHORES COMPLETE!!=====")
print("Great work finishing your entire checklist today!\n")

print("Now let's safely peek at the infinite loop....")
test_value = 0
safetyvalue = 0
while test_value <= 0:
    print("This condition never changes, so this would run forever!")
    safetyvalue += 1
    if safetyvalue == 3:
        print("Stopping on purpose - a real infinite loop goes on forever on its own !")
        break

print()
print("=====CHORE CHECKLIST SUMMARY=====")
print("Chores assigned today :", original_count)
print("Chores remaining :", total_chores - completed_count)
print("=================================")
