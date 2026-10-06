class Device:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)

class Smartphone(Device):
    def __init__(self, brand, model, camera, storage):
        super().__init__(brand, model)
        self.camera = camera
        self.storage = storage

    def display(self):
        print("----- Smartphone Details -----")
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Camera:", self.camera, "MP")
        print("Storage:", self.storage, "GB")

phone = Smartphone("Apple", "Iphone 17 pro", 48, 1000)
phone.display()

print("Is Smartphone a subclass of Device??", issubclass(Smartphone, Device))

