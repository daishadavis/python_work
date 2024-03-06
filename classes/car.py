class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Intializing attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted description name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's milage"""
        print(f"This car had {self.odometer_reading} miles on it")
    
    def update_odometer(self, milage):
        """
        Set the odometer reading to give value.
        Reject the change if it tries to roll the odometer back.
        """
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You can't roll back the odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles



my_used_car = Car('subaru', 'outback', '2015')
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
