import logging
import time
from slackclient import SlackClient

class SlackBotHandler:
    def __init__(self, repo, slack_token, bot_name):
        self.__bot_name = bot_name
        self.__repo = repo
        self.__client = SlackClient(slack_token)

    def get_message_info(self, event):
        return event['channel'], event['user'], event['text'][len(self.__bot_name) + 1:].strip()


    def reply(self, event):
        channel, user, message = self.get_message_info(event)
        try:
            message = self.__repo.get_card_path(message)
        except Exception as e:
            message = "Unable to find card you requested, sorry."
            logging.info(e)
        self.__client.server.channels.find(channel).send_message(message)


    def monitor(self):
        if self.__client.rtm_connect():
            while True:
                events = self.__client.rtm_read()
                try:
                    if len(events) == 0:
                        logging.debug("No events. Sleeping...")
                        time.sleep(1)
                    for event in events:
                        logging.info("Received an event with text: ")
                        logging.info(event)
                        if event['type'] == 'message' and event['text'].startswith(self.__bot_name):
                            self.reply(event)
                except Exception as e:
                    logging.error("Invalid event received")
                    logging.error(e)
