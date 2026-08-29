def calculate_total(price, quntity):
    return price * quantity
def apply_discount(total):
    if total >= 2000:
        return total * 0.10 #10% discount
    else:
        return 0 

def display_bill(customer_name, total, discount, final_amount):
    print("\n -----SHOPPING BILL-----")
    print("Customer Name :", customer_name)
    print("Total Amount:", total)
    print("Discount :", discount)
    print("Final amount :", final_amount)

customer_name = input("Enter Customer Name:")
item_name = input("Enter item name:")
price = float(input("Enter Price per item :"))
quantity = int(input("Enter Quantity :"))

total = calculate_total(price, quantity)
discount = apply_discount(total)
final_amount = total - discount
display_bill(customer_name, total, discount, final_amount)
