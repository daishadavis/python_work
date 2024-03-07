"""A set if classes used to represent gas and electric cars."""

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


class Battery:
    """A simple attempt to a model a battery for an electric car."""
    def __init__(self, battery_size=75):
        """Initializing the battery attributes."""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kwh battery.")

    def get_range(self):
        """Print statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """Setting the battery capacity to 100."""
        if self.battery_size != 100:
            self.battery_size = 100

class ElectricCar(Car):
    """
    Initialize attributes of the parent class.
    Then initalize attributes specific to an electric car.
    """    
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class"""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks"""
        print("This car doesn't need a gas tank!")
    
my_tesla = ElectricCar('tesla', 'model s', '2019')

