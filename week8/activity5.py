class TravelPackage:
    def __init__(self, destination, hotel, transport, mealplan, activities, insurance):
        self.destination = destination
        self.hotel = hotel
        self.transport = transport
        self.mealplan = mealplan
        self.activities = activities
        self.insurance = insurance

    def show_travel_package(self):
        print("Destination:", self.destination)
        print("Hotel:", self.hotel)
        print("Transport:", self.transport)
        print("Meal Plan:", self.mealplan)
        print("Activities:", self.activities)
        print("Insurance:", self.insurance)

class TravelPackageBuilder:
    def __init__(self):
        self.destination = None
        self.hotel = None
        self.transport = None
        self.mealplan = None
        self.activities = None
        self.insurance = None

    def set_destination(self, destination):
        self.destination = destination
        return self

    def set_hotel(self, hotel):
        self.hotel = hotel
        return self

    def set_transport(self, transport):
        self.transport = transport
        return self

    def set_mealplan(self, mealplan):
        self.mealplan = mealplan
        return self

    def add_activities(self, activities):
        self.activities = activities
        return self

    def set_insurance(self, insurance):
        self.insurance = insurance
        return self

    def build(self):
         return TravelPackage(
            self.destination,
            self.hotel,
            self.transport,
            self.mealplan,
            self.activities,
            self.insurance
         )
         
         
travel_package = (
    TravelPackageBuilder()
    .set_destination("Antarctica")
    .set_hotel("3 star hotel")
    .set_transport("Flight and Cruise")
    .set_mealplan("All-Inclusive")
    .add_activities(["Tour", "Snorkeling", "Hiking"])
    .set_insurance(True)
    .build())

travel_package.show_travel_package()