class Card:
    def __init__(self, data):
        # NOTE: only surfacing relevant fields from the API
        self.__code = data['code']
        self.__faction_code = data['faction_code']
        self.__keywords = data['keywords']
        self.__text = data['text']
        self.__title = data['title']
        self.__type_code = data['type_code']
        self.__side_code = data['side_code']

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

