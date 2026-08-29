def greetcustomer():
    print("Welcome to the Lemonade Stand!")
    print("Fresh Lemonade, made just for you.")

greetcustomer()
price_per_cup = float(input("Enter the price per cup in dollars :"))
cups_sold = int(input("Enter the number of cups sold :"))

def calculate_total(price, cups):
    total = price * cups
    return total
total_cost = calculate_total(price_per_cup, cups_sold)
rounded_total = round(total_cost, 2)

print("Total Cost :", rounded_total)
amount_paid = float(input("Enter the amount paid by the customer :"))
def calculate_change(paid,total):
    change = paid - total
    return change 

change_due = calculate_change(amount_paid, rounded_total)
rounded_change = round(change_due)

def thank_message(cups):
    if cups >= 5:
        return "Wow, big order! Thank you so much for your support!"

    else:
        return "Thanks for stopping by the stand!"

closing_message = thank_message(cups_sold)

print()
print("===== LEMONADE STAND RECIEPT =====")
print("Price per cup :", price_per_cup)
print("Cups sold:", cups_sold)
print("Total Cost :", total_cost)
print("Amount Paid:", amount_paid)
print("Change Due :", change_due)
print(closing_message)
print("==================================")