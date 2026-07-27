#today we will make school club member badge 
name = input("Enter your name: ")
club = input("Enter your club name: ")

#storing details of student using different datatypes 
Class = type(input("Enter your class: "))
birth_date = input("Enter your birthdate: ")
address = input("Enter your address: ")
agent_number = int(input("Enter your agent number: "))
age = int(input("Enter your age: "))

# printing each data type with its data type
print("Name:", name, type(name))
print("Club:", club, type(club))
print("Class:", Class, type(Class))
print("Birth Date:", birth_date, type(birth_date))
print("Address:", address, type(address))
print("Agent Number:", agent_number, type(agent_number))
print("Age:", age, type(age))

#typecasting the number into text 
agent_number_text = str(agent_number)
club_text = str(club)
age_as_text = str(age)

#printing typecaested data types 
print("Agent Number in text:", agent_number_text, type(agent_number_text))
print("Club in text:", club_text, type(club_text))
print("Age in text:", age_as_text, type(age_as_text))

#slicing the name to create a badge id 
first_three_letters = name[0:3]
last_two_letters = name[-2:]
badge_id = first_three_letters + last_two_letters 

#reverse the club name using slicing to create a badge code
reversed_club_code = club[::-1]
print("Your badge id is:", badge_id)
print("Your badge code is:", reversed_club_code)

#join everything to crate the school club member badge 
badge_line_1 = "NAME: " + name.upper() + " | CLUB: " + club.upper()
badge_line_2 = "CLASS: " + str(Class) + " | BIRTH DATE: " + birth_date.upper()
badge_line_3 = "ADDRESS: " + address.upper() + " | AGE: " + str(age)
badge_line_4 = "AGENT NUMBER: " + str(agent_number)
badge_line_5 = "BADGE ID: " + badge_id.lower() + " | BADGE CODE: " + reversed_club_code

#displaying the school club member badge 
print("\n\n")
print("<<<<<<<<<<<<<<<<<SCHOOL CLUB MEMBER BADGE>>>>>>>>>>>>>>")
print(badge_line_1)
print(badge_line_2)
print(badge_line_3)
print(badge_line_4)
print(badge_line_5)
print("==================================================")
