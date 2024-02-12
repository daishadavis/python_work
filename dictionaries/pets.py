pet_0 = {'animal': 'dog', 'owner': 'jake'}
pet_1 = {'animal': 'cat', 'owner': 'sarah'}
pet_2 = {'animal': 'snake', 'owner': 'malcolm'}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    print(f"The pet is a {pet['animal']}. The owner is {pet['owner'].title()}")