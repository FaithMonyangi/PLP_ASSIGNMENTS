class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.__price = price  # Private attribute (Encapsulation)

    # Method to display phone details
    def specs(self):
        return f"{self.brand} {self.model} - ${self.__price}"

    # Getter for price (Encapsulation)
    def get_price(self):
        return self.__price

    # Setter for price (Encapsulation with basic validation)
    def set_price(self, new_price):
        if new_price >= 0:
            self.__price = new_price
        else:
            print("Invalid price! Must be 0 or higher.")

    # Magic method for printing the object nicely
    def __str__(self):
        return self.specs()
phone = Smartphone("Apple", "iPhone 15", 1299)
print(phone)  # Apple iPhone 15 - $1299

print("Current price:", phone.get_price())  # 1299

phone.set_price(1199)
print("Updated price:", phone.get_price())  # 1199

phone.set_price(-500)  # Invalid price!

# Base class for Vehicle
class Vehicle:
    def move(self):
        pass  # This is a placeholder method, to be overridden

# Car class
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Plane class
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Boat class
class Boat(Vehicle):
    def move(self):
        print("Sailing 🚢")

# Test the polymorphism
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()  # Each object calls its own move() method

