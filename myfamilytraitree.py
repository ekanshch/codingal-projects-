class FamilyMember:
    def __init__(self, eye_color, height_cm):
        self.eye_color = eye_color
        self.height_cm = height_cm

    def show_traits(self):
        print("Eye Color:", self.eye_color)
        print("Height (cm):", self.height_cm)

class Kid(FamilyMember):
    def __init__(self, name, age, eye_color, height_cm):
        self.name = name
        self.age = age  
        super().__init__(eye_color, height_cm)  


    def show_traits(self):
        print("Name:", self.name)
        print("Age:", self.age)
        super().show_traits()

    def favourite_hobby(self, hobby):
        print(f"{self.name}'s favourite hobby is {hobby}.")

child = Kid("Alice", 10, "Blue", 30)
child.show_traits()
child.favourite_hobby("Drawing")

print("Is kid a subclassm of FamilyMember??", issubclass(Kid, FamilyMember))