from datetime import datetime
import logging

from netrunnerdb.card import Card


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

    def get_card_by_id(self, identifier):
        return next(filter(lambda x: x.code == identifier, self.__cards))

    def get_card_by_title(self, title):
        return next(filter(lambda x: title in x.title, self.__cards))

    def get_card_by_match(self, query):
        it = self.__cards
        for field in query.split():
            it = filter(lambda x: (x.matches_query(field.lower())), it)

        return next(it)

    @property
    def version_number(self):
        return self.__version_number

    @property
    def last_updated(self):
        return self.__last_updated
