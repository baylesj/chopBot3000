import yaml
import os
import logging


class QueryConfig:
    expected_keys = {"weights": ["full_title", "partial_title", "full_text", "partial_text", "default"]}

    def __init__(self, config_path="./query/queryconfig.yml"):
        if not os.path.isfile(config_path):
            logging.critical('Unable to load the configuration file')
            raise FileNotFoundError

        with open(config_path, 'r') as yml_file:
            cfg = yaml.load(yml_file)

        self.__weights = cfg['weights']

    @property
    def full_title_weight(self):
        return self.__weights['full_title']

    @property
    def keyword_weight(self):
        return self.__weights['keyword']

    @property
    def partial_title_weight(self):
        return self.__weights['partial_title']

    @property
    def full_text_weight(self):
        return self.__weights['full_text']

    @property
    def partial_text_weight(self):
        return self.__weights['partial_text']

    @property
    def default_weight(self):
        return self.__weights['default']
