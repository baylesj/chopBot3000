import logging
import os
import time

from slackclient import SlackClient

import logging
logger = logging.getLogger(__name__)

def get_message_info(event, bot_name):
    return event['channel'], event['user'], event['text'][len(bot_name) + 1:].strip()


def reply(event, bot_name, client, repo):
    channel, user, message = get_message_info(event, bot_name)
    try:
        message = repo.get_card_path(message)
    except Exception as e:
        message = "Unable to find card you requested, sorry."
    client.server.channels.find(channel).send_message(message)


def monitor(repo):
    # TODO: get this from API
    bot_name = "<@U2J5GAF96>"
    token = os.environ["CHOPBOT_3000_TOKEN"]
    client = SlackClient(token)

    if client.rtm_connect():
        while True:
            events = client.rtm_read()
            try:
                if len(events) == 0:
                    logger.debug("No events. Sleeping...")
                    time.sleep(1)
                for event in events:
                    logger.info("Received an event with text: ")
                    logger.info(event)
                    if event['type'] == 'message' and event['text'].startswith(bot_name):
                        reply(event, bot_name, client, repo)
            except Exception as e:
                logger.error("Invalid event received")
                logger.error(e)
