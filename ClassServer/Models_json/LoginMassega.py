from pykson import JsonObject, StringField


class LoginMessage(JsonObject):
    email = StringField()
    password = StringField()
