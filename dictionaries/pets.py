#pet_0 = {'animal': 'dog', 'owner': 'jake'}
#pet_1 = {'animal': 'cat', 'owner': 'sarah'}
#pet_2 = {'animal': 'snake', 'owner': 'malcolm'}

#pets = [pet_0, pet_1, pet_2]

#for pet in pets:
    #print(f"The pet is a {pet['animal']}. The owner is {pet['owner'].title()}")

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

def describe_pet(pet_name,animal_type='dog'):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")

#Ways to call a function.
describe_pet('willie')
describe_pet(pet_name='willie')

describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')