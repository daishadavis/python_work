person_0 = {'first_name': 'daisha', 'last_name': 'davis', 'age': 26, 'city': 'New York'}
person_1 = {'first_name': 'daniel', 'last_name': 'davis', 'age': 24, 'city': 'New York'}
person_2 = {'first_name': 'rachel', 'last_name': 'davis', 'age': 42, 'city': 'New York'}

people = [person_0, person_1, person_2]

for person in people:
    for k, v in person.items():
        print(f"{k}: {v}")
    print("\n")