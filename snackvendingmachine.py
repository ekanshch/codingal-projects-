def calculate_change(paid, price):
    change = paid - price
    return change
snack_price = 30
print("===== SNACK VENDING MACHINE =====")
print(f"Snack Price: {snack_price} units")
print("Accepted coins: 1, 5, 10, 25\n")

total_inserted = 0
coins_inserted = 0
while True:
    coin = int(input("Insert coin (1, 5, 10, 25) : "))
    if coin != 1 and coin!= 5 and coin != 10 and coin != 25:
        print("Invalid coin. Please try again.")
        continue
    total_inserted += coin
    coins_inserted += 1
    print(f"Inserted {coin}. Total inserted so far: {total_inserted}\n")
    if total_inserted >= snack_price:
        print("Enough money inserted.")
        break

change_due = calculate_change(total_inserted, snack_price)

print("Dispensing your snack...")

if change_due == 0:
    pass
else:
    print(f"Here is your change: {change_due} units")

print("\n =====PURCHASE SUMMARY=====")
print(f"Snack Price: {snack_price} units")
print(f"Total Paid: {total_inserted} units")
print(f"Coins Inserted: {coins_inserted}")
print(f"Change Given: {change_due} units")
print("===== THANK YOU FOR YOUR PURCHASE! =====")