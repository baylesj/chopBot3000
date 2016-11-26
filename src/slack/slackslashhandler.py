import logging

class SlackSlashHandler:
    def __init__(self, card_repo):
        self.__card_repo = card_repo

    def get_matching_card(self, query):
        try:
            message = repo.get_card_path(query)
        except Exception as e:
            message = "Unable to find the card you requested, sorry."
            logging.info(e)
        return message

