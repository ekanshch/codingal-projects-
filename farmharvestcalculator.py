# we will make a farm harvest calculator 
field1= 120
field2= 150
field3= 200
field4= 30
field5= 50

total = field1 + field2 + field3 + field4 + field5
average = total / 5

print("Total harvest is :", total, "kg")
print("Average harvest per field is :", average, "kg")
price_per_kg = 30
earnings = total * price_per_kg
print("Total earnings : Rs.", earnings)

bags = total // 30
leftover = total % 30
print("Full bags packed :", bags)
print("Leftover grain :", leftover)

last_year = 370
print("Better than last year ?", total > last_year)
print("Same as last year ?", total == last_year)
print("At least as good as last year ?", total >= last_year)
#adding bonus crop
total += 30
print("After bonus crop :", total, "kg")
#subtracting 15kg seeds for next season
total -= 15
print("After reserving seeds :", total,"kg")
#final bag count after all adjustments 
bags = total // 30
print("Final bags packed :", bags)
