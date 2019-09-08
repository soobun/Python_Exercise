import unittest
from CH_11.city_functions import city_country_format


class CityTest(unittest.TestCase):
    def test_city_country(self):
        format_result = city_country_format('shanghai', 'china')
        self.assertEqual(format_result, 'Shanghai, China')

    def test_city_country_plus(self):
        format_result = city_country_format('shanghai', 'china', 24237800)
        self.assertEqual(format_result, 'Shanghai, China - population 24237800')


unittest.main()
