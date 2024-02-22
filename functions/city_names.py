def city_country(city, country):
    """Return formatted city, country name"""
    return f"{city.title()}, {country.title()}"

print(city_country("New York", "united states"))
print(city_country("Rio", "brazil"))
print(city_country("paris", "france"))