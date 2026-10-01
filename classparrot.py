class Parrot:
    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age

Ronaldo = Parrot("Ronaldo", 5)
Messi = Parrot("Messi", 30)

print("Ronaldo is a {}".format(Ronaldo.species))
print("Messi is a {}".format(Messi.species))
print("{} is {} years old".format(Ronaldo.name, Ronaldo.age))
print("{} is {} years old".format(Messi.name, Messi.age))
