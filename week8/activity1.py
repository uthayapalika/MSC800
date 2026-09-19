class Pizza:
    def speak(self):
        print("I'm a pizza!")

class Burger:
    def speak(self):
        print("I'm a burger!")

class Pasta:
    def speak(self):
        print("I'm a pasta!")

# Factory
class RestaurantFactory:
    @staticmethod
    def create_food(food_type):
        if food_type == "pizza":
            
            return Pizza()
        elif food_type == "burger":
            return Burger()
        elif food_type == "pasta":
            return Pasta()
        else:
            raise ValueError("Unknown food")

food = RestaurantFactory.create_food("pizza")
food.speak()