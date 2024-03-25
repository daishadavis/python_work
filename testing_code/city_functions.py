def get_city_country(city, country, population=''):
    """Format the name country and population"""
    if population:
        city_country = f"{city}, {country} - population {population}"
    else:
        city_country = f"{city}, {country}"
    return city_country.title()