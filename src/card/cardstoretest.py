import unittest
from datetime import datetime
from datetime import timedelta

from card.cardstore import CardStore


class CardStoreTest(unittest.TestCase):
    def _build_body(self, last_updated, version_number, cards):
        return {'last_updated' : last_updated,
                'version_number' : version_number,
                'data' : cards}

    def test_invalid_last_updated_sets_to_now(self):
        body = self._build_body("I am not valid", False, [])

        actual = CardStore(body).last_updated
        expected = datetime.now()

        self.assertTrue(actual - expected < timedelta(seconds=1))

    def test_valid_version_number(self):
        valid_version = "1337"
        valid_date = '2016-09-22T02:39:48+00:00'
        body = self._build_body(valid_date, valid_version, [])

        actual = CardStore(body).version_number

        self.assertEqual(valid_version, actual)

    def test_valid_last_updated(self):
        valid_string = '2016-09-22T02:39:48+00:00'
        expected = datetime(2016, 9, 22, 2, 39, 48)

        body = self._build_body(valid_string, False, [])
        actual = CardStore(body).last_updated

        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
