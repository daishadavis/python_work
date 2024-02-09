#Using the get() method for checking if key exist
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'no point value assigned') 
print(point_value)

person = {'first_name': 'daisha', 'last_name': 'davis', 'age': 26, 'city': 'New York'}

print(person['first_name'].title())
print(person['last_name'].title())
print(person['age'])
print(person['city'].title())

favorite_numbers = {
    'daisha': 5,
    'daniel': 17,
    'ema': 4,
    'rachel': 3,
    'aba': 16
}

print(f"Daisha's favorite number is {favorite_numbers['daisha']}")
print(f"Daniel's favorite number is {favorite_numbers['daniel']}")
print(f"Ema's favorite number is {favorite_numbers['ema']}")
print(f"Rachel's favorite number is {favorite_numbers['rachel']}")
print(f"Aba's favorite number is {favorite_numbers['aba']}")

glossary = {
    'variable': 'a container for storing data',
    'string': 'sequence of characters wrapped in quotes',
    'boolean': 'truth values - either True or False',
    'list': 'mutable, order sequence of elements',
    'tuples': 'immuable, order sequence of values',
    'integer': 'whole numbers',
}

for key, value in glossary.items():
    print(f"{key.title()}: {value}")