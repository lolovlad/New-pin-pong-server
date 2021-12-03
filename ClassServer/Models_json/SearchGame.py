from pykson import JsonObject, StringField, IntegerField, ObjectField
from Class.Network import NetWork


class SearchGameMessage(JsonObject):
    id_user = IntegerField()
    color = StringField()
    ip = StringField()
    port = IntegerField()
