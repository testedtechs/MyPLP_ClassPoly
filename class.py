# Base class: Superhero
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        return f"I am {self.name}, and I protect {self.city} with my power: {self.power}!"

    def use_power(self):
        return f"{self.name} uses {self.power}!"

# Subclass: FlyingHero inherits from Superhero
class FlyingHero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.flight_speed = flight_speed

    def use_power(self):
        return f"{self.name} flies at {self.flight_speed} km/h while using {self.power}!"

# Subclass: StrengthHero inherits from Superhero
class StrengthHero(Superhero):
    def __init__(self, name, power, city, strength_level):
        super().__init__(name, power, city)
        self.strength_level = strength_level

    def use_power(self):
        return f"{self.name} lifts objects weighing up to {self.strength_level} tons with {self.power}!"
