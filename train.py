class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def start_engine(self):
        print(f"The {self.brand} {self.model}'s engine is starting.")

# Creating objects (instances) of the Car class
car1 = Car("Toyota", "Camry")
car2 = Car("Ford", "Mustang")

# Accessing attributes and calling methods
print(car1.brand)              # Output: Toyota
print(car2.model)              # Output: Mustang

car1.start_engine()            # Output: The Toyota Camry's engine is starting.
car2.start_engine()            # Output: The Ford Mustang's engine is starting.
