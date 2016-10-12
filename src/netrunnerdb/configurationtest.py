import unittest

from netrunnerdb.configuration import Configuration


class ConfigurationTest(unittest.TestCase):
    def test_invalid_file(self):
        with self.assertRaises(FileNotFoundError):
            Configuration(False)

    def test_get_card_property_exists(self):
        self.assertTrue(Configuration().get_card)

    def test_get_cards_property_exists(self):
        self.assertTrue(Configuration().get_cards)

    def test_get_card_png_property_exists(self):
        self.assertTrue(Configuration().get_card_png)

    def test_cache_max_age_in_seconds_property_exists(self):
        self.assertTrue(Configuration().cache_max_age_in_seconds)

if __name__ == "__main__":
    unittest.main()
