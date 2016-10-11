import yaml
import os
import logging

class Configuration:
    def __init__(self, config_path="config.yml"):
        if not os.path.isfile(config_path):
            logging.critical('Unable to load the configuration file')
            raise FileNotFoundError

        self.load_configuration(config_path)

    def load_configuration(self, config_path):
        with open(config_path, 'r') as yml_file:
            cfg = yaml.load(yml_file)

        self.__server = "{}{}{}".format(cfg['server']['protocol'],
                              cfg['server']['domain'],
                              cfg['server']['api_root'])

        self.__get_card = "{}{}".format(self.__server, cfg['rest']['get_card'])
        self.__get_cards = "{}{}".format(self.__server, cfg['rest']['get_cards'])
        self.__get_card_png = "{}{}".format(self.__server,
                cfg['non_rest']['get_card_png'])
        self.__cache_max_age = cfg['cache']['max_age_in_seconds']

    @property
    def get_card(self):
        return self.__get_card

    @property
    def get_cards(self):
        return self.__get_cards

    @property
    def get_card_png(self):
        return self.__get_card_png

    @property
    def cache_max_age_in_seconds(self):
        return self.__cache_max_age
