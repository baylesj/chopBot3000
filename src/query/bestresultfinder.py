from query.queryranker import QueryRanker

import logging
logger = logging.getLogger(__name__)


class BestResultFinder:
    def __init__(self, card_store):
        self.__card_store = card_store
        self.__cache = {}
        self.__ranker = QueryRanker()

    def get_best_match(self, query):
        if query not in self.__cache:
            self.__cache[query] = self.__get_max_scored_card(query)

        return self.__cache[query]

    # TODO: optimize here. O(N) is not ideal.
    def __get_max_scored_card(self, query):
        max_score = 0
        max_location = None
        for i in range(len(self.__card_store.get_all_cards())):
            score = self.__ranker.get_card_score(self.__card_store.get_card_by_index(i), query)
            if score > max_score:
                max_location = i
                max_score = score

        logger.info("Card query return location {}, score {}".format(max_location, max_score))

        return self.__card_store.get_card_by_index(max_location)