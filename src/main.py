import os
import logging
import sys
import getopt
import time

from flask import Flask
import flask
from slackclient import SlackClient
from netrunnerdb.cardrepository import CardRepository
from slack.slackslashhandler import SlackSlashHandler

app = Flask(__name__)


def initialize_logging(log_level):
    logFormatter = logging.Formatter("%(asctime)-.19s [%(levelname)-7.15s]:  %(message)s")
    rootLogger = logging.getLogger()
    rootLogger.setLevel(getattr(logging, log_level.upper()))

    fileHandler = logging.FileHandler("chopbot.log")
    fileHandler.setFormatter(logFormatter)
    rootLogger.addHandler(fileHandler)

    consoleHandler = logging.StreamHandler(sys.stdout)
    consoleHandler.setFormatter(logFormatter)
    rootLogger.addHandler(consoleHandler)


def get_message_info(event, bot_name):
    return event['channel'], event['user'], event['text'][len(bot_name) + 1:].strip()


def reply(event, bot_name, client, repo):
    channel, user, message = get_message_info(event, bot_name)
    try:
        message = repo.get_card_path(message)
    except Exception as e:
        message = "Unable to find card you requested, sorry."
        logging.info(e)
    client.server.channels.find(channel).send_message(message)


def monitor(repo, bot_name, client):
    if client.rtm_connect():
        while True:
            events = client.rtm_read()
            try:
                if len(events) == 0:
                    logging.debug("No events. Sleeping...")
                    time.sleep(1)
                for event in events:
                    logging.info("Received an event with text: ")
                    logging.info(event)
                    if event['type'] == 'message' and event['text'].startswith(bot_name):
                        reply(event, bot_name, client, repo)
            except Exception as e:
                logging.error("Invalid event received")
                logging.error(e)

def print_help():
    print('{0} [ -L|--log_level=[INFO|WARNING|ERROR] ]'.format(sys.argv[0]))


@app.route('/', methods=['POST'])
def hello_world():
    return flask.jsonify(handler.get_matching_card(flask.request))

if __name__ == "__main__":
    log_level = "WARNING"
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hL:",["log_level="])
    except getopt.GetoptError:
        print("Error parsing options.")
        print_help()
        sys.exit(2)
    print(opts)
    for opt, arg in opts:
        if opt == '-h':
            print_help()
            sys.exit()
        elif opt in ("-L", "--log_level"):
            log_level = arg

    initialize_logging(log_level)
    logging.warning("Starting application...")

    # TODO: get this from API
    #bot_name = "<@U378QUALE>"
    #
    #if "SLACK_BOT_TOKEN" not in os.environ:
    #    logging.error("SLACK_BOT_TOKEN environment variable not provided!")
    #    sys.exit(-1)
    #token = os.environ["SLACK_BOT_TOKEN"]
    
    repo = CardRepository()
    #client = SlackClient(token)
    handler = SlackSlashHandler(repo)

    #monitor(repo, bot_name, client)
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)

    logging.warning("Exiting application...")


