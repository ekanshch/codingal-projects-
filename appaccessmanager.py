# we will create a student app access manager
CAMERA = 1 #0001
MICROPHONE = 2 #0010
STORAGE = 4 #0100
LOCATION = 8 #1000
#list of available apps for students
approved_apps = [
    "coding app",
    "drawing app",
    "math app",
    "reading app",
    "science app"
]
#student details
student_name = input("Enter student name: ")

requested_app = input("Enter the app you want to access: ").lower()

print("\n\n")
print("---------IDNTITY OPERATOR CHECKER---------")

if type(student_name) is str:
    print("Student name is stored as text")

if type(requested_app) is not str:
    print("The requested app is not stored as a number")

print("\n\n")
print("---------MEMBERSHIP OPERATOR CHECK---------")

if requested_app in approved_apps:
    print(requested_app + " is an approved app for students")

else:
    print(requested_app + " is not an approved app for students")

restricted_apps = [
    "social media app",
    "gaming app",
    "shopping app",
    "video streaming app"
]

if requested_app not in restricted_apps:
    print("The app is not in the restricted list.")

else:
   print("Access denied because app is restricted for students")

print("\n\n")
print("---------APP PERMISSION SETTINGS---------")

students_permission = CAMERA | MICROPHONE | STORAGE | LOCATION

print("Permission Value:", students_permission)
print("Permission Bits:", bin(students_permission))

if students_permission & CAMERA:
    print("Camera access is granted")

if students_permission & MICROPHONE:
    print("Microphone access is granted")

if students_permission & STORAGE:
    print("Storage access is granted")

if students_permission & LOCATION:
    print("Location access is granted")
else:
    print("Location access is denied")

print("\n\n")
print("---------BIT SHIFT DEMONSTRATION---------")

next_permission = CAMERA << 1
print("Camera bit:", bin(CAMERA))
print("After left shift:", bin(next_permission))

previous_permission = STORAGE >> 1
print("Storage bit:", bin(STORAGE))
print("After right shift:", bin(previous_permission))

print("\n\n")
print("---------FINAL ACCESS RESULT---------")

if requested_app in approved_apps and requested_app not in restricted_apps:
    print("Access granted to:", requested_app)
else:
    print("Access denied to:", requested_app)
print("-"*37)