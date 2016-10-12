import os
import logging

from slackclient import SlackClient
from netrunnerdb.cardrepository import CardRepository


def get_message_info(event, bot_name):
    return event['channel'], event['user'], event['text'][len(bot_name) + 1:].strip()


def reply(event, bot_name, client, repo):
    channel, user, message = get_message_info(event, bot_name)
    try:
        message = repo.get_card_path(message)
    except Exception as e:
        message = "Unable to find card you requested, sorry."
    client.server.channels.find(channel).send_message(message)


def monitor(repo, bot_name, client):
    if client.rtm_connect():
        while True:
            events = client.rtm_read()
            try:
                for event in events:
                    if event['type'] == 'message' and event['text'].startswith(bot_name):
                        reply(event, bot_name, client, repo)
            except Exception as e:
                logging.error("Invalid event received")


def main():
    repo = CardRepository()

    # TODO: get this from API
    bot_name = "<@U2J5GAF96>"
    os.environ["SLACK_BOT_TOKEN"] = "xoxb-86186355312-OonGNYEHhEPpgFxgC1lQClxz"
    token = os.environ["SLACK_BOT_TOKEN"]
    client = SlackClient(token)

    monitor(repo, bot_name, client)

    logging.warning("Exiting application...")


if __name__ == "__main__":
    main()
