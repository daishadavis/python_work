from random import randint

class Dice:
    """A simple class to present a dice"""

    def __init__(self, sides=10):
        """Initalizing attributes."""
        self.sides = sides

    def roll_die(self):
        """Simulate rolling a dice"""
        print(randint(1, self.sides))


die = Dice(10)
for _ in range(0, 10):
    die.roll_die()
