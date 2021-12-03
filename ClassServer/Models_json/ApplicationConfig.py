from pykson import JsonObject, ObjectField
from ClassServer.Models_json import DataBase


class ApplicationConfig(JsonObject):
    data_base = ObjectField(DataBase)
