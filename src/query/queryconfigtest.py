import unittest

from query.queryconfig import QueryConfig


class QueryConfigTest(unittest.TestCase):
    def setUp(self):
        self.__valid_config = QueryConfig("queryconfig.yml")

    def test_invalid_file(self):
        with self.assertRaises(FileNotFoundError):
            QueryConfig(False)

    def test_full_title_weight_property_exists(self):
        self.assertTrue(self.__valid_config.full_title_weight)

    def test_keyword_weight_property_exists(self):
        self.assertTrue(self.__valid_config.keyword_weight)

    def test_partial_title_weight_property_exists(self):
        self.assertTrue(self.__valid_config.partial_title_weight)
        
    def test_full_text_weight_property_exists(self):
        self.assertTrue(self.__valid_config.full_text_weight)
        
    def test_partial_text_weight_property_exists(self):
        self.assertTrue(self.__valid_config.partial_text_weight)
        
    def test_default_weight_property_exists(self):
        self.assertTrue(self.__valid_config.default_weight)


if __name__ == '__main__':
    unittest.main()
