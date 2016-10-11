from datetime import datetime
import logging
from card import Card

class CardStore:
    def __init__(self, cards_response):
        self.__cache_cards(cards_response)

    def __cache_cards(self, cards_response):
        try:
            version_number = cards_response['version_number']
            last_updated = self.__parse_datetime(cards_response['last_updated'])
            cards = self.__parse_cards(cards_response['data'])
        except Exception as e:
            logging.error("Failed to update cache! Leaving old data", e)
        else:
            self.__version_number = version_number
            self.__last_updated = last_updated
            self.__cards = cards

    def __parse_cards(self, cards):
        cards = []
        for card_data in cards:
            cards.append(Card(card_data))
        return cards

    def __parse_datetime(self, string):
        try:
            return datetime.strptime(string.split("+")[0], "%Y-%m-%dT%H:%M:%S")
        except ValueError:
            return datetime.now()

    def get_all_cards(self):
        return self.__cards

    def get_card_by_id(self, identifier):
        return filter(lambda x: x.code == identifier, self.__cards)

    @property
    def version_number(self):
        return self.__version_number

    @property
    def last_updated(self):
        return self.__last_updated

