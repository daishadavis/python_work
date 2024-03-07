class User:
    """Creating a user profile"""

    def __init__(self, first_name, last_name, age, location):
        """Create the Intial attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0

    def user_info(self):
        """Summarize user profile"""
        print(f"My name is {self.first_name.title()} {self.last_name.title()}")
        print(f"I am {self.age} years old")
        print(f"I live in {self.location.title()}")

    def greet_user(self):
        """Greet the user"""
        print(f"Hello {self.first_name.title()} it's nice to meet you!")

    def increment_login_attempts(self):
        """Adding one to the number of login attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resetting the number of login attempts to zero."""
        self.login_attempts = 0

class Admin:
    """Creating and admin with special privilages"""

    def __init__(self, first_name, last_name, age, location, privileges):
        """Initalize admin class and attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.privilages = Privilages(privileges)

class Privilages:
    """Showing the privilages of an admin."""
    def __init__(self, privilages):
        self.privilages = privilages

    def show_privilages(self):
        """Display admin privilages"""
        print(f"These are the admins privilages:")
        for privilage in self.privilages:
            print(f"-{privilage}")





        


