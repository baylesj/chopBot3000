import requests
from configuration import Configuration

class NetrunnerClient:
    def __init__(self):
        self.__config = Configuration()

    def __get_response(self, url):
        response = requests.get(url)
        if response.status_code != 200:
            raise ApiError('Request at "{}" raised {}'
                    .format(url, response.status_code))

        return response

    def __get_json_response(self, url):
        return self.__get_response(url).json()

    def get_card(self, card_id):
        url = self.__config.get_card.format(card_id)
        return self.__get_json_response(url)

    def get_cards(self):
        return self.__get_json_response(self.__config.get_cards)

    def get_card_png(self, card_id):
        url = self.__config.get_card_png.format(card_id)
        return self.__get_response(url)
