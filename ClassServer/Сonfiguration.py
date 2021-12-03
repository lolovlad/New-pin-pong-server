import json
from pathlib import Path

from pykson import Pykson
from ClassServer.Models_json.ApplicationConfig import ApplicationConfig


class Configuration:
    def __init__(self, configuration_file_name):
        self.__name_dir = "Files"
        dir_path = Path(Path(__file__).parent).parent
        self.__path = Path(dir_path,  self.__name_dir, configuration_file_name)
        self.__config = {}

    def load(self):
        with open(self.__path, "r") as read_file:
            self.__config = json.load(read_file)
            application_config = Pykson().from_json(self.__config, ApplicationConfig)
            return application_config

    def save(self):
        with open(self.__path, 'w') as outfile:
            json.dump(self.__config, outfile)

