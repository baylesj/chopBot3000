import unittest
from datetime import datetime
from datetime import timedelta

class CardTest(unittest.TestCase):
    def _build_body(self, last_updated, version_number, cards):
        return {'last_updated' : last_updated,
                'version_number' : version_number,
                'data' : cards}

    def test_invalid_last_updated_sets_to_now(self):
        pass

if __name__ == "__main__":
    unittest.main()
