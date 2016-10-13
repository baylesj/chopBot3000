import logging
from datetime import datetime

from card.card import Card

logger = logging.getLogger(__name__)


class CardStore:
    def __init__(self, cards_response):
        self.__cache_cards(cards_response)

    def __cache_cards(self, cards_response):
        try:
            version_number = cards_response['version_number']
            last_updated = self.__parse_datetime(cards_response['last_updated'])
            cards = self.__parse_cards(cards_response['data'])
        except Exception as e:
            logger.error("Failed to update cache! Leaving old data", e)
        else:
            self.__version_number = version_number
            self.__last_updated = last_updated
            self.__cards = cards

    @staticmethod
    def __parse_cards(cards_data):
        cards = []
        for card_data in cards_data:
            cards.append(Card(card_data))

        logging.info("Parsed {} cards".format(len(cards)))

        return cards

    @staticmethod
    def __parse_datetime(string):
        try:
            return datetime.strptime(string.split("+")[0], "%Y-%m-%dT%H:%M:%S")
        except ValueError:
            return datetime.now()

    def get_all_cards(self):
        return self.__cards

    def get_card_by_index(self, index):
        return self.__cards[index]

    @property
    def version_number(self):
        return self.__version_number

    @property
    def last_updated(self):
        return self.__last_updated
