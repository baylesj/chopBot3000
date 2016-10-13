from card.cardstore import CardStore
from netrunnerdb.clientconfig import ClientConfig
from netrunnerdb.netrunnerdbclient import NetrunnerDbClient


class CardRepository:
    def __init__(self):
        self.__client = NetrunnerDbClient()
        self.__config = ClientConfig()
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
