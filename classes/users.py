class User:
    """Creating a user profile"""

    def __init__(self, first_name, last_name, age, location):
        """Create the Intial attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location

    def user_info(self):
        """Summarize user profile"""
        print(f"My name is {self.first_name.title()} {self.last_name.title()}")
        print(f"I am {self.age} years old")
        print(f"I live in {self.location.title()}")

    def greet_user(self):
        """Greet the user"""
        print(f"Hello {self.first_name.title()} it's nice to meet you!")



daisha = User('daisha', 'davis', 26, 'new york city')
daisha.user_info()
daisha.greet_user()
print("----")

charlie = User('charlie', 'puth', 32, 'los angeles')
charlie.user_info()
charlie.greet_user()
print("----")

dana = User('dana', 'fairbanks', 25, 'los angeles')
dana.user_info()
dana.greet_user()
print("---")