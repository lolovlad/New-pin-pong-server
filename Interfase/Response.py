from pykson import Pykson


class Response:
    @staticmethod
    def parser_message(message, model):
        return Pykson().from_json(message, model)