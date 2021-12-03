from pykson import JsonObject, StringField, IntegerField


class Player(JsonObject):
    color = StringField()
    ip = StringField()
    port = IntegerField()
