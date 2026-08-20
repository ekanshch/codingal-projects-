print("=== ATM Cash Dispenser ===\n")
t_100 = t_50 = t_20 = t_10 = t_5 = t_1 = 0
customerserved = 0
totaldispense = 0

serving = True 
while serving:
    name= input("Enter customer name :")
    amount = int(input(f"Hello {name}, Enter withdrawal amount :"))
    if amount <= 0:
        print("Invalid amount.. Please enter a positive number\n")
        continue
    print(f"\n Dispensing {amount} units for {name}")
    remaining = amount
    idx = 1
    while idx <= 6:
        if idx == 1 : value = 100
        elif idx == 2: value = 50
        elif idx == 3: value = 20
        elif idx == 4: value = 10
        elif idx == 5: value = 5
        else: value = 1
        count = remaining // value
        if count > 0:
            print(f" {count} x {value}-unit note(s) = {count*value}")
            remaining -= count * value
            if value == 100: t_100 += count
            elif value == 50: t_50 += count
            elif value == 20: t_20 += count
            elif value == 10: t_10 += count
            elif value == 5: t_5 += count
            else: t_1 += count
        idx += 1

    customerserved += 1
    totaldispense += amount
    print(f"Transactionn complete, {name}! \n")
    again = input("Next customer? (yes/no) :").strip().lower()
    if again != "yes":
        serving = False

print("\n ===Daily Denomination Report===")
for slot in range(1, 7):
    if slot == 1: value, total = 100, t_100
    elif slot == 2: value, total = 50, t_50
    elif slot == 3: value, total = 20, t_20
    elif slot == 4: value, total = 10, t_10
    elif slot == 5: value, total = 5, t_5
    else: value, total = 1, t_1
    if total > 0:
        print(f"{value}-unit notes dispensed : {total}", end="")
        for note in range(total):
            print("=", end="")
        print()

print("Customers served :", customerserved)
print("Total amount dispensed :", totaldispense)
print("ATM session closed. Goodbye!")

