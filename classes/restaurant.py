class Restaurant:
    """A simple restaurant class"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initalize restaurant name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print information about the restaurant"""
        print(f"The name of this restaurant is {self.restaurant_name}")
        print(f"They serve {self.cuisine_type} here.")

    def open_restaurant(self):
        """Print a message indicating the restaurant is open"""
        print(f"{self.restaurant_name} is offically open for the day!")


chinese_restaurant = Restaurant('Ollies', 'Chinese food')
italian_restaturant = Restaurant('Carmens', 'Italian food')
korean_restaurant = Restaurant('99 Favor', 'Korean BBQ')

chinese_restaurant.describe_restaurant()
print("---")
italian_restaturant.describe_restaurant()
print("---")
korean_restaurant.describe_restaurant()
