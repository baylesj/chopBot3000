#!/usr/bin/env python3
import logging
import sys
import getopt

from slack.monitor import monitor
from slack.slackslashhandler import SlackSlashHandler
from cardrepository import CardRepository
from flask import Flask
from flask import request
import flask

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
    print()
    print('{0} [ -L|--log_level=[INFO|WARNING|ERROR] -b ]'.format(sys.argv[0]))
    print()
    print('     -b')
    print('             Operate in legacy bot mode rather than slash command.')


@app.route('/', methods=['POST'])
def serve_matching_card():
    return flask.jsonify(handler.get_matching_card(flask.request))

if __name__ == "__main__":
    log_level = "WARNING"
    should_use_bot = False
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hbL:",["log_level="])
    except getopt.GetoptError:
        print("Error parsing options.")
        print_help()
        sys.exit(2)
    
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
        monitor(repo)
    else:
        handler = SlackSlashHandler(repo)
        app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)

    logging.warning("Exiting application...")


