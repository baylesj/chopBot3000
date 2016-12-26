from query.queryconfig import QueryConfig
import logging


class QueryRanker:
    def __init__(self, config=None):
            self.__config = config or QueryConfig()

    @staticmethod
    def __sanitize_query(query):
        return query.strip().lower()

    def get_card_score(self, card, query):
        query = self.__sanitize_query(query)
        if not query:
            return 0

        return self.__calculate_weight(card, query)

    def __calculate_weight(self, card, query):
        weight = self.__get_title_weight(card, query)
        weight += self.__get_text_weight(card, query)
        weight += self.__get_other_weight(card, query)
        weight += self.__get_keyword_weight(card, query)
        return weight

    def __get_text_weight(self, card, query):
        if query == card.text.lower():
            return self.__config.full_text_weight
        elif query in card.text.lower():
            return self.__config.partial_text_weight
        return 0

    def __get_keyword_weight(self, card, query):
        keywords = [x.lower() for x in card.keywords.split()]
        if set(query.split()) <= set(keywords):
            return self.__config.keyword_weight
        return 0

    def __get_title_weight(self, card, query):
        if query == card.title.lower():
            return self.__config.full_title_weight
        elif query in card.title.lower():
            return self.__config.partial_title_weight
        return 0

    def __get_other_weight(self, card, query):
        for field in [card.flavor.lower(),
                      card.faction_code.lower(),
                      card.side_code.lower(),
                      card.type_code.lower()]:
            if query in field:
                return self.__config.default_weight
        return 0
