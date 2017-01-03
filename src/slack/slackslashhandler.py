import logging

class SlackSlashHandler:
    def __init__(self, card_repo):
        self.__card_repo = card_repo

    def format_response(self, message):
        response = {}
        response['response_type'] = 'in_channel'
        response['text'] = message
        return response

    def parse_message_text(self, request):
        # Sample request:
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
        logging.debug(request.form)
        return request.form['text']

    def get_matching_card(self, request):
        query = self.parse_message_text(request)
        try:
            message = self.__card_repo.get_card_path(query)
        except Exception as e:
            message = "Unable to find the card you requested, sorry."
            logging.info(e)
        return self.format_response(message)
