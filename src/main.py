#!/usr/bin/env python3
import logging
import sys
import getopt

from slack.monitor import monitor
from slack.slackslashhandler import SlackSlashHandler
from cardrepository import CardRepository
from flask import Flask
from flask import request

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
def serve_matching_card():
    print(request.form)
    # token=gIkuvaNzQIHg97ATvDxqgjtO
    # team_id=T0001
    # team_domain=example
    # channel_id=C2147483705
    # channel_name=test
    # user_id=U2147483697
    # user_name=Steve
    # command=/weather
    # text=94070
    # response_url=https://hooks.slack.com/commands/1234/5678
    for key in request.form:
        print("Key: "+key)
        print(request.form[key])
    #return 'Hello world'
    return handler.get_matching_card(request.form['text'])

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

    repo = CardRepository()
    #client = SlackClient(token)
    handler = SlackSlashHandler(repo)

    #monitor(repo)
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)

    logging.warning("Exiting application...")


