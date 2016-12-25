import unittest

from netrunnerdb.clientconfig import ClientConfig


class ClientConfigTest(unittest.TestCase):
    def setUp(self):
        self.__valid_config = ClientConfig("clientconfig.yml")

    def test_invalid_file(self):
        with self.assertRaises(FileNotFoundError):
            ClientConfig(False)

    def test_get_card_property_exists(self):
        self.assertTrue(self.__valid_config.get_card)

    def test_get_cards_property_exists(self):
        self.assertTrue(self.__valid_config.get_cards)

    def test_get_card_png_property_exists(self):
        self.assertTrue(self.__valid_config.get_card_png)

    def test_cache_max_age_in_seconds_property_exists(self):
        self.assertTrue(self.__valid_config.cache_max_age_in_seconds)

if __name__ == "__main__":
    unittest.main()
