#!/usr/bin/env python3
import logging
import sys
import getopt

from slack.monitor import monitor
from cardrepository import CardRepository


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


def main():
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
    monitor(repo)

    logging.warning("Exiting application...")


if __name__ == "__main__":
    main()
