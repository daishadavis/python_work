favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")


for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")


print("The following languages have been mentioned:")
for language in set  (favorite_languages.values()):
    print(language.title())

languages = {'python', 'ruby', 'python', 'c'}
print(languages)

rivers = {'nile': 'egypt', 'amazon river': 'brazil', 'congo river': 'africa'}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")

print("\n")

for river in rivers.keys():
    print(river)

print("\n")

for country in rivers.values():
    print(country)


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

people = ['jen', 'edward', 'michelle']

for person in people:
   if person in favorite_languages.keys():
       print(f"Thank you {person.title()} for taking our poll.")
else:
    print(f"Hello, {person.title()} would you like to take our poll?")


favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")