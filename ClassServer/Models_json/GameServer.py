import random
import socket
import struct

#socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))


class GameServer:
    def __init__(self, id_server):
        self.__port = random.randint(5000, 9999)
        self.__ip = "localhost"
        self.__id_server = id_server
        self.__players = []
        self.__state = "void"

    def add_player(self, player):
        self.__players.append(player)
        self.change_state()

    def change_state(self):
        if len(self.__players) == 1:
            self.state = "one player"
        elif len(self.__players) == 2:
            self.state = "playing"

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, val):
        self.__state = val

    @property
    def port(self):
        return self.__port

    @property
    def ip(self):
        return self.__ip

    @property
    def id(self):
        return self.__id_server
