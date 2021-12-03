from Interfase.Singleton import Singleton
from Interfase.Observer import Subject


class ListGameServer(Subject):
    __metaclass__ = Singleton
    __dict_server_game = {}
    __list_observers = []

    def append(self, server):
        self.__dict_server_game[server.id] = server
        self.notify(self.__dict_server_game)

    def remove(self, server):
        self.__dict_server_game.pop(server.id)

    def attach(self, observer):
        self.__list_observers.append(observer)

    def detach(self, observer):
        self.__list_observers.remove(observer)

    def notify(self, struct):
        for observer in self.__list_observers:
            observer.update(struct)

    def get_void_game_server(self):
        return list(filter(lambda x: x.state == "void", self.__dict_server_game.values()))

    def get_one_player_game_server(self):
        return list(filter(lambda x: x.state == "one player", self.__dict_server_game.values()))

    def get_playing_game_server(self):
        return list(filter(lambda x: x.state == "playing", self.__dict_server_game.values()))

    def __len__(self):
        return len(self.__dict_server_game)
