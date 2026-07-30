# we will create a pizza shop billing system 
#we will take pizza's sold in 5 hours 
first_hour = int(input("Enter no. of pizza sold in first hour :"))
second_hour = int(input("Enter no. of pizza sold in second hour :"))
third_hour = int(input("Enter no. of pizza sold in third hour :"))
fourth_hour = int(input("Enter no. of pizza sold in fourth hour :"))
fifth_hour = int(input("Enter no. of pizza sold in fifth hour :"))
total = first_hour + second_hour + third_hour + fourth_hour + fifth_hour
average = total / 5
print("Total pizza's sold in five hours :", total)
print("Average pizza's sold per hour is :", average)
price_per_pizza = 250
earnings = total * 250
print("Total earnings : Rs", earnings)
boxes = total // 8
leftover = total % 8
print("Full boxes packed :", boxes)
print("Leftover pizza's :", leftover)

last_day_sale = 100
print("Better than last day sales ??", total > last_day_sale)
print("Same as last day sales ??", total == last_day_sale)
print("Atleast as good as last day ??", total >= last_day_sale)

#adding more pizza sale recieved afterwards
total += 12
print("total pizza sales after 5 hours :", total)
# 5 orders were cancelled 
total -= 5
print("Total pizza sales after subtracting cancelled orders :", total)
#final pizza sales
boxes = total // 8
print("Total boxes packed :", boxes)