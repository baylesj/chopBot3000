from cardstore import CardStore
from netrunnerclient import NetrunnerClient
from configuration import Configuration

class CardRepository:
    def __init__(self):
        self.__client = NetrunnerClient()
        self.__config = Configuration()
        self.__store = CardStore(self.__client.get_cards())

    def get_store(self):
        return self.__store
