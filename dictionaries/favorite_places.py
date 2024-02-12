favorite_places = {
    'peter': ['new york', 'london'],
    'daisha': ['tokyo', 'paris'],
    'ryan': ['lima', 'rome']
}

for name, places in favorite_places.items():
    print(f"{name.title()}'s favortie places are:")
    for place in places:
        print(f"\t{place.title()}")
    print("\n")