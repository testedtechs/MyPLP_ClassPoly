# Base class: Vehicle
class Vehicle:
    def move(self):
        return "The vehicle moves."

# Subclass: Car
class Car(Vehicle):
    def move(self):
        return "Driving on the road 🚗."

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        return "Flying in the sky ✈️."

# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        return "Sailing across the water 🚤."

# Test polymorphism
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    print(vehicle.move())
