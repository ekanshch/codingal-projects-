# taking the temprature
temprature = int(input("Enter the temprature in Celcius :"))
#deciding to wear a jacket or a t-shirt
if temprature < 20:
    outfit = "jacket"
    print("Weather is cold today.")
    print("Wear a ", outfit)
else:
    outfit = "t-shirt"
    print("Weather is warm today.")
    print("Wear a ", outfit)
#ask whether it is raining 
is_raining = input("Is it raining today ?(yes/no) :")
#add an umbrella if it is raining 
if is_raining == "yes" :
    print("Bring an umbrella.")
#ask for wind speed
wind_speed = int(input("Enter the wind speed in km/h :"))
if  wind_speed > 30 :
    needs_windbreaker = "yes"
    print("It is windy today.")
    print("Wear a windbreaker over your ", outfit)
else:
    needs_windbreaker = "no"
    print("It is calm today.")
    print("There is no need to wear windbreaker over your ", outfit)
#ask whether there are puddles on the ground 
has_puddles = input("Are there puddles on the ground ? (yes/no):")
#decide between boots or sneakers 
if has_puddles == "yes":
    shoes = "boots"
    print("The ground is wet.")
    print("Wear ", shoes)
else :
    shoes = "sneakers"
    print("The ground is dry.")
    print("Wear ", shoes)

print("WEATHER CHECK IS COMPLETE")
print("/n/n")

print("=======WEATHER OUTFIT PICKER=======")
print("Temprature:", temprature)
print("Outfit chosen:", outfit)
print("Raining:", is_raining)
print("Windbreaker needed:", needs_windbreaker)
print("Shoes chosen:", shoes)
print("===================================")
