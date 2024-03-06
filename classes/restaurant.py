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


chinese_restaurant = Restaurant('Ollies', 'Chinese food')
italian_restaturant = Restaurant('Carmens', 'Italian food')
korean_restaurant = Restaurant('99 Favor', 'Korean BBQ')


chinese_restaurant.describe_restaurant()
print("---")
italian_restaturant.describe_restaurant()
print("---")
korean_restaurant.describe_restaurant()



restaurant = Restaurant('chiptole', 'mexican')
restaurant.set_number_served(30)
restaurant.increment_number_served(40)
print(f"\nNumber served: {restaurant.number_served}")