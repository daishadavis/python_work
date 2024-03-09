class Character:
    """A class used to represent a video game character."""

    def __init__(self, name, fighter_type, weapon, speed, moves):
        self.name = name
        self.fighter_type = fighter_type
        self.weapon = weapon
        self.speed = speed
        self.moves = moves
        self.health = 100
    
    def health_reading(self):
        """Show a character's current health"""
        print(f"This is the characters current health: {self.health}")

    def take_damage(self, damage=20):
        """Show the damage the character has taken."""
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name.title()} took {damage} and now has {self.health} health.")

    def show_moves(self):
        """Print each move a character has."""
        print("Here are their moves:")
        for move in self.moves:
            print(f"-{move}")

    def summary(self):
        """Print a summary about the character"""
        print("This is the complete character summary:")
        print(f"Name: {self.name.title()}, Fightertype: {self.fighter_type.title()}, Weapon: {self.weapon.title()}")

    


warrior = Character('june', 'warrior', 'blade', 80, ['flying kick', 'back kick', 'power move', 'body slam'])
ninja = Character('shadow', 'ninja', 'sword', 95, ['sword slice', 'sword stab', 'front kick', 'back kick', 'power move'])

ninja.summary()
ninja.health_reading()
ninja.take_damage()
