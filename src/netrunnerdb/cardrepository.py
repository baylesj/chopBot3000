from netrunnerdb.cardstore import CardStore
from netrunnerdb.configuration import Configuration
from netrunnerdb.netrunnerclient import NetrunnerClient


class CardRepository:
    def __init__(self):
        self.__client = NetrunnerClient()
        self.__config = Configuration()
        self.__store = CardStore(self.__client.get_cards())

    def get_store(self):
        return self.__store

    def get_card_by_title(self, title):
        return self.__store.get_card_by_title(title)

    def get_card_path(self, query):
        card = self.get_store().get_card_by_match(query)
        if card:
            return self.__config.get_card_png.format(card.code)

        return None
