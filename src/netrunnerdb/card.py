import logging

class Card:
    def __init__(self, data):
        # NOTE: only surfacing relevant fields from the API
        try:
            self.__code = data['code']

            self.__keywords = data.get('keywords', '')
            self.__text = data.get('text', '')
            self.__title = data.get('title', '')
            self.__side_code = data.get('side_code', '')
            self.__type_code = data.get('type_code', '')
            self.__faction_code = data.get('faction_code', '')
        except KeyError as e:
            logging.warning("Invalid card: {} is missing".format(e))

    def matches_query(self, query):
        return query in self.code.lower() \
            or query in self.keywords.lower() \
            or query in self.text.lower() \
            or query in self.title.lower()

    @property
    def code(self):
        return self.__code

    @property
    def faction_code(self):
        return self.__faction_code

    @property
    def keywords(self):
        return self.__keywords

    @property
    def text(self):
        return self.__text

    @property
    def title(self):
        return self.__title

    @property
    def type_code(self):
        return self.__type_code

    @property
    def side_code(self):
        return self.__side_code

    def __str__(self):
        return "Card name: " + self.title

