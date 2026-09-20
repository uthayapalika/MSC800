# ==========================================
# 1. PRODUCT
# ==========================================
class BasicCar:

    def cost(self):
        return 25000

    def description(self):
        return "Basic Car"


# ==========================================
# 2. BASE DECORATOR
# ==========================================
class CarDecorator:

    def __init__(self, car):
        self.car = car

    def cost(self):
        return self.car.cost()

    def description(self):
        return self.car.description()


# ==========================================
# 3. CONCRETE DECORATORS
# ==========================================

class GPSDecorator(CarDecorator):

    def cost(self):
        return self.car.cost() + 500

    def description(self):
        return self.car.description() + " + GPS"


class SunroofDecorator(CarDecorator):

    def cost(self):
        return self.car.cost() + 1000

    def description(self):
        return self.car.description() + " + Sunroof"


class LeatherSeatsDecorator(CarDecorator):

    def cost(self):
        return self.car.cost() + 1500

    def description(self):
        return self.car.description() + " + Leather Seats"


class PremiumSoundDecorator(CarDecorator):

    def cost(self):
        return self.car.cost() + 800

    def description(self):
        return self.car.description() + " + Premium Sound System"


# ==========================================
# 4. CLIENT
# ==========================================

# Basic car
car = BasicCar()

print(car.description())
print("Total Price: $", car.cost())


# Add GPS
car = GPSDecorator(car)

# Add Sunroof
car = SunroofDecorator(car)

# Add Leather Seats
car = LeatherSeatsDecorator(car)

# Add Premium Sound System
car = PremiumSoundDecorator(car)


print("\nCustomised Car:")
print(car.description())
print("Total Price: $", car.cost())