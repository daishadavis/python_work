import unittest
from city_functions import get_city_country

class CityTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'"""

    def test_city_country(self):
        """Does Santiago, Chile work?"""
        city_country = get_city_country('santiago', 'chile')
        self.assertEqual(city_country, 'Santiago, Chile')

    def test_city_country_population(self):
        """Test that optional population argument works properly."""
        city_country = get_city_country('santiago', 'chile', '5000000')
        self.assertEqual(city_country, 'Santiago, Chile - Population 5000000')

if __name__ == '__main__':
    unittest.main()