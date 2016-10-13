import logging

from cardrepository import CardRepository
from slack.monitor import monitor


def main():
    repo = CardRepository()

    monitor(repo)

    logging.warning("Exiting application...")


if __name__ == "__main__":
    main()
