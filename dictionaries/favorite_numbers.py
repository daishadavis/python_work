favortie_numbers = {
    'peter': [3, 7],
    'bob': [3, 5],
    'logan': [6, 9, 15]
}

for name, number in favortie_numbers.items():
    print(f"{name.title()}'s favorite numbers are:")
    print(f"\t{number}")
    print("\n")
