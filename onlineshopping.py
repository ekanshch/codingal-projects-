def calculate_bill(price, quantity):
    return price * quantity
grand_total = 0
while True:
    product = input("Enter product name (or type exit to finish): ")
    if product.lower() == "exit":
        print("\nThank you for shopping with us!")
        break
    quantity = int(input(f"Enter quantity for {product}: "))
    if quantity <= 0:
        print("Quantity must be greater than 0. Please try again.")
        continue
    price = float(input(f"Enter price for {product}: "))
    bill = calculate_bill(price, quantity)
    grand_total += bill
    print("Product:", product)
    print("Bill ", bill)
    pass


print("\n===== FINAL BILL =====")
print(f"Grand Total: {grand_total}")