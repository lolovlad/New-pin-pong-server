from Core.GameСreator import GameCreator
from Model.Player import Player
from Model.DataBase import DataBase
from ClassServer import StartApplication as app
from socket import *
from threading import Thread
from Core.Network import NetWork
from Resourses.Login import Login
from Resourses.Registration import Registration


app().context_validation_and_creation()

sock = socket()
sock.bind(('localhost', 2510))
sock.listen(6)

gc = GameCreator()
DataBase().attach(gc)


def client_core(socket_client):
    global gc
    network_core = NetWork(socket_client)
    while True:
        message = network_core.listener()
        type_message = message.pop("type_request")
        message_return = ""
        if type_message == "login":
            message_return = Login.post(message)
        elif type_message == "registration":
            message_return = Registration.post(message)
        elif type_message == "start_search_game":
            user = Player(message["Name_user"], message["Ip_user"], message["Mmr_user"], network_core)
            if len(DataBase().get_observer()) > 2:
                for i in DataBase().get_observer():
                    DataBase().detach(i)
                DataBase().attach(gc)
            gc.colors.append(message["Color"])
            DataBase().attach(user)
            while True:
                command = user.network.listener()
                if command is not None:
                    DataBase().add_list_command(command)
                else:
                    break
        network_core.send_message(message_return)


while True:
    print('connection...')
    client, mass = sock.accept()
    print(mass, 'connect')
    Thread(target=client_core, args=(client,), daemon=True).start()
