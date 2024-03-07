"""A class that can be use to represent a restaurant."""
class Restaurant:
    """A simple restaurant class"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initalize restaurant name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Print information about the restaurant"""
        print(f"The name of this restaurant is {self.restaurant_name}")
        print(f"They serve {self.cuisine_type} here.")

    def open_restaurant(self):
        """Print a message indicating the restaurant is open"""
        print(f"{self.restaurant_name} is offically open for the day!")

    def set_number_served(self, guests):
        """Set the number of served customers to a given value"""
        self.number_served = guests

    def increment_number_served(self, increment):
        """Add a given number to the total customers served."""
        self.number_served += increment

class IceCreamStand(Restaurant):
    """A simple ice cream stand"""
    
    def __init__(self, restaurant_name, cuisine_type, flavors):
        """
        Initalizing attributes of the parent class.
        Then initalizing attributes specifc to an ice cream stand.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        """Display ice cream flavor"""
        print(f"The flavors are:")
        for flavor in self.flavors:
            print(f"-{flavor}")

