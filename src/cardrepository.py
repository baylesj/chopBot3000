from card.cardstore import CardStore
from netrunnerdb.clientconfig import ClientConfig
from netrunnerdb.netrunnerdbclient import NetrunnerDbClient

import logging

from query.bestresultfinder import BestResultFinder

logger = logging.getLogger(__name__)


class CardRepository:
    def __init__(self):
        self.__client = NetrunnerDbClient()
        self.__config = ClientConfig()
        self.__store = CardStore(self.__client.get_cards())
        self.__finder = BestResultFinder(self.__store)

    def get_store(self):
        return self.__store

    def get_card_path(self, query):
        card = self.__finder.get_best_match(query)
        if card:
            return self.__config.get_card_png.format(card.code)

        logging.warning("Failed to get valid card path for: " + query)
        return None
