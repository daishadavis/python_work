class Employee:
    """A class representing an Employee"""

    def __init__(self,first_name,last_name,salary):
        """Initalizing attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, salary_raise=5000):
        """Adds $5000 dollars to the annual salary"""
        self.salary += salary_raise