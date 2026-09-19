customer1 = {"cheese", "pepperoni", "cheese", "mushroom", "olive"}
customer2 = {"olive", "paneer", "pepperoni", "paneer"}

print("Customer 1:  ", customer1)
print("Customer 2:  ", customer2)

customer1.add("capsicum")
print("Customer 1 after adding capsicum: ", customer1)

common_topping = customer1.intersection(customer2)

print("Common Toppings :", common_topping)

import array as arr
pizza_sales = arr.array('i', [12, 15, 10, 18])

print("Pizza Sales Array :", pizza_sales)

pizza_sales.insert(0, 8)
pizza_sales.append(20)

print("Updated Pizza Sale:", pizza_sales)
count_18 = pizza_sales.count(18)
print("Number of times 18 appears : ", count_18)
pizza_sales.reverse()

print("Reversed Sales Array:  ", pizza_sales)


print("\n===== PIZZA TOPPINGS ORGANIZER =====")
print("Customer 1 Toppings:  ", customer1)
print("Customer 2 Toppings:  ", customer2)
print("Common Toppings:  ", common_topping)
print("Pizza Sales:  ", pizza_sales)
print("======================================")