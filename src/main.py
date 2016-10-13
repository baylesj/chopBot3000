#!/usr/bin/env python3

import logging

from cardrepository import CardRepository
from slack.monitor import monitor


logging.basicConfig(filename='chopbot3000.log', level=logging.DEBUG)
logger = logging.getLogger(__name__)


def main():
    repo = CardRepository()

    monitor(repo)

    logger.warning("Exiting application...")


if __name__ == "__main__":
    main()
