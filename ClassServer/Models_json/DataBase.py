from pykson import JsonObject, StringField


class DataBase(JsonObject):
    type_database = StringField()
    name_database = StringField()
    default_name_database = StringField()
    default_dir_database = StringField()