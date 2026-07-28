# making a student id card using python 
from datetime import datetime
name = input("Enter your name: ")
student_id = input("Enter your student id: ")
birth_date = input("Enter your birthdate (YYYY-MM-DD): ")
class_name = input("Enter your class: ")
blood_group = input("Enter your blood group: ")
phone_number = int(input("Enter your phone number: "))
birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
# Get today's date
today = datetime.today()
# Calculate age
age = today.year - birth_date.year
#If birthday has not occurred yet this year, subtract 1
if (today.month, today.day) < (birth_date.month, birth_date.day): age -= 1

#printing ech data type with its data type 
print("Name:", name, type(name))
print("Student ID:", student_id, type(student_id))  
print("Birth Date:", birth_date, type(birth_date))
print("Class:", class_name, type(class_name))
print("Blood Group:", blood_group, type(blood_group))
print("Phone Number:", phone_number, type(phone_number))
print("Age:", age, type(age))

#printing the student id card
id_card_line_1 = "NAME: " + name.upper() + " | STUDENT ID: " + student_id.upper()
id_card_line_2 = "BIRTH DATE: " + birth_date.strftime("%d-%m-%Y")
id_card_line_3 = "CLASS: " + class_name.upper() + " | BLOOD GROUP: " + blood_group.upper()
id_card_line_4 = "PHONE NUMBER: " + str(phone_number)
id_card_line_5 = "AGE: " + str(age)

print("\n\n")
print("<<<<<<<<<<<<<<<<<STUDENT ID CARD>>>>>>>>>>>>>>")
print(id_card_line_1)
print(id_card_line_2)  
print(id_card_line_3)
print(id_card_line_4)
print(id_card_line_5)
print("==================================================")