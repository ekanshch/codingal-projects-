print("-----SCHOOL ADMISSION PORTAL-----")

name = input("Enter your name :")

count = 0
for ch in name:
    count = count + 1

reverse_name = ('')

for ch in name:
    reverse_name = ch + reverse_name

n = int(input("Enter registration number :"))

total = 0 

for i in range(1, n+1):
    total = total + i 


print()
print("-----ADMIMISSION REPORT-----")
print("Student name :", name)
print("Number of characters:", count)
print("Reverse name:", reverse_name)
print("registration number :", n)
print("registration sum :", total)
