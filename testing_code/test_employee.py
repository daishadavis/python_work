import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for class Employee"""

    def setUp(self):
        """Create an Employee entry with first aname, last name, and salary for all method use"""
        first_name = 'Jane'
        last_name = 'Doe'
        self.salary = 5000
        self.employee = Employee(first_name, last_name, self.salary)

    def test_give_default_raise(self):
        """Test that the defauklt raise works properly."""
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, self.salary + 5000)

    def test_give_custom_raise(self):
        """Test that custom raise works properly."""
        custom_raise = 10000
        self.employee.give_raise(custom_raise)
        self.assertEqual(self.employee.salary, self.salary + custom_raise)

if __name__ == '__main__':
    unittest.main()