cities = {
    'paris':{
        'country':'france',
        'population': 2_000_000,
        'fact': 'Its believed that Paris has one stop sign in the entire city',
    },
    'tokyo':{
        'country': 'japan',
        'population': 13_000_000,
        'fact': 'You can purchase almost anything from a vending machine in Tokyo',
    },
    'sydney':{
        'country': 'australia',
        'population': 5_000_000,
        'fact': 'Sydney has over 100 beaches',
    },
}

for city, information in cities.items():
    print(f"{city.title()}'s is located in {information['country']}, has a population of {information['population']} million.")
    print(f"Fun fact about {city.title()}: {information['fact']}.\n")