import unittest
from unittest.mock import MagicMock, PropertyMock

from card.card import Card
from query.queryconfig import QueryConfig
from query.queryranker import QueryRanker


class QueryRankerTest(unittest.TestCase):
    def setUp(self):
        self.__mock_config = MagicMock(())
        type(self.__mock_config).full_title_weight = PropertyMock(return_value=10000)
        type(self.__mock_config).keyword_weight = PropertyMock(return_value=5000)
        type(self.__mock_config).partial_title_weight = PropertyMock(return_value=1000)
        type(self.__mock_config).full_text_weight = PropertyMock(return_value=100)
        type(self.__mock_config).partial_text_weight = PropertyMock(return_value=10)
        type(self.__mock_config).default_weight = PropertyMock(return_value=1)

        self.__ranker = QueryRanker(self.__mock_config)

    def test_empty_query_weight_zero(self):
        card = _CardBuilder.build_card('1337')
        self.assertEqual(0, self.__ranker.get_card_score(card, ""))

    def test_full_title_match(self):
        card = _CardBuilder.build_card('1337', title='Fancy Title')
        self.assertEqual(10000, self.__ranker.get_card_score(card, 'Fancy title'))

    def test_keyword_single_match(self):
        card = _CardBuilder.build_card('1337', keywords='Dominion')
        self.assertEqual(5000, self.__ranker.get_card_score(card, 'Dominion'))

    def test_partial_title_match(self):
        card = _CardBuilder.build_card('1337', title='Something Really Hard To Remember!')
        self.assertEqual(1000, self.__ranker.get_card_score(card, 'Hard to Remember'))

    def test_text_match(self):
        card = _CardBuilder.build_card('1337', text='Suprisingly short!')
        self.assertEqual(100, self.__ranker.get_card_score(card, 'Suprisingly short!'))

    def test_text_partial_match(self):
        card = _CardBuilder.build_card('1337', text='This is not Suprisingly short!')
        self.assertEqual(10, self.__ranker.get_card_score(card, 'Suprisingly short!'))

    def test_flavor_match(self):
        card = _CardBuilder.build_card('1337', flavor='Umami')
        self.assertEqual(1, self.__ranker.get_card_score(card, 'Umam'))
        self.assertEqual(1, self.__ranker.get_card_score(card, 'Umami'))

    def test_faction_code_match(self):
        card = _CardBuilder.build_card('1337', faction_code='Umami')
        self.assertEqual(1, self.__ranker.get_card_score(card, 'Umam'))
        self.assertEqual(1, self.__ranker.get_card_score(card, 'Umami'))

    def test_side_code_match(self):
        card = _CardBuilder.build_card('1337', side_code='Umami')
        self.assertEqual(1, self.__ranker.get_card_score(card, 'Umam'))
        self.assertEqual(1, self.__ranker.get_card_score(card, 'Umami'))

    def test_type_code_match(self):
        card = _CardBuilder.build_card('1337', type_code='Umami')
        self.assertEqual(1, self.__ranker.get_card_score(card, 'Umam'))
        self.assertEqual(1, self.__ranker.get_card_score(card, 'Umami'))


class _CardBuilder:
    @staticmethod
    def build_card(code, flavor='', keywords='', text='', title='',
                   side_code='', type_code='', faction_code=''):
        return Card({'code': code,
                     'flavor': flavor,
                     'keywords': keywords,
                     'text': text,
                     'title': title,
                     'side_code': side_code,
                     'type_code': type_code,
                     'faction_code': faction_code
                     })



if __name__ == '__main__':
    unittest.main()
