import os
import logging
import sys
import getopt

from flask import Flask
import flask
from netrunnerdb.cardrepository import CardRepository
from slack.slackslashhandler import SlackSlashHandler
from slack.slackbothandler import SlackBotHandler

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


def print_help():
    print('{0} [ -L|--log_level=[INFO|WARNING|ERROR] ]'.format(sys.argv[0]))


@app.route('/', methods=['POST'])
def hello_world():
    return flask.jsonify(handler.get_matching_card(flask.request))

if __name__ == "__main__":
    log_level = "WARNING"
    should_use_bot = False

    try:
        opts, args = getopt.getopt(sys.argv[1:],"hL:b",["log_level="])
    except getopt.GetoptError:
        print("Error parsing options.")
        print_help()
        sys.exit(2)
    print(opts)
    for opt, arg in opts:
        if opt == '-h':
            print_help()
            sys.exit()
        elif opt == '-b':
            should_use_bot = True
        elif opt in ("-L", "--log_level"):
            log_level = arg

    initialize_logging(log_level)
    logging.warning("Starting application...")

    
    repo = CardRepository()
    if should_use_bot:
        # TODO: get this from API
        bot_name = "<@U378QUALE>"
        
        if "SLACK_BOT_TOKEN" not in os.environ:
            logging.error("SLACK_BOT_TOKEN environment variable not provided!")
            sys.exit(-1)
        token = os.environ["SLACK_BOT_TOKEN"]
        bot_handler = SlackBotHandler(repo, token, bot_name)
        bot_handler.monitor()
    else:
        handler = SlackSlashHandler(repo)
        app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)

    logging.warning("Exiting application...")


