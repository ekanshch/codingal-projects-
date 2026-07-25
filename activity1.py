# ask the agent for their details 
name = input("Enter your name :")
gadget = input("Enter your favourite gadget :")

# storing agents details using different data types 
agent_number = 30
speed_rating = 7.8
height_m = 1.37
mission_count = 10
is_active = True

#print each detail along with its data type 
print("Name:", name, "-> Type:", type(name))
print(" Gadget:", gadget, "-> Type:", type(gadget))
print("Agent number:", agent_number,"-> Type:", type(agent_number))
print("Speed rating:", speed_rating, "-> Type:", type(speed_rating))
print("Height (m):", height_m, "-> Type:", type(height_m))
print("Mission Count:", mission_count, "->Type:", type(mission_count))
print("Is Active:", is_active, "-> Type:", type(is_active))

#typecast the numbers and true/fase values into text 
agent_number_text = str(agent_number)
speed_rating_text = str(speed_rating)
mission_count_text = str(mission_count)
status_text = str(is_active)

print("Agent Number as text :", agent_number_text, "-> Type:", type(agent_number_text))
print("Speed Rating as text :", speed_rating_text, "-> Type:", type(speed_rating_text))
print("Mission Count as text :", mission_count_text, "-> Type:", type(mission_count_text))
print("Status as text :", status_text, "-> Type:", type(status_text))

#slice the name to create a secret code name 
first_three = name[0:3]
last_letter = name[-1]
code_name = first_three + last_letter
print("First three letters of your name:", first_three)
print("Last letter of your name:", last_letter)
print("Your secret code name is:", code_name)

#reverse the gadget name using slicing 
reversed_gadget = gadget[::-1]
print("Reversed gadget name :", reversed_gadget)

#join everything together to create a final badge message 
badge_line_1 = "AGENT:" + code_name.upper()
badge_line_2 = "ID:" + agent_number_text + "| MISSIONS:" + mission_count_text

#print complete secret agent badge 
print("")
print("==========Secret Agent==========")
print(badge_line_1)
print(badge_line_2)
print("================================")
