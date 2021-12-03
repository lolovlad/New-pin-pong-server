from Models import User
from Interfase.Response import Response
from Class.Models_json.SearchGame import SearchGameMessage
from Class.Models_json.GameServer import GameServer
from Class import StartApplication as app
from Class.ListGameServer import ListGameServer
from Class.Models_json.Player import Player
from pykson import Pykson


class StartSearchGame(Response):
    @classmethod
    def post(cls, message, net):
        args = Pykson().from_json(message, SearchGameMessage)
        list_player = ListGameServer()
        massage = {}
        user_database = app().context.query(User).filter(User.id == args.id_user).first()
        player = Pykson().from_json({"color": args.color,
                                     "ip": args.ip,
                                     "port": args.port}, Player)
        player.user = user_database
        player.network = net
        if len(list_player.get_void_game_server()) > 0:
            game_server_void = list_player.get_void_game_server()[0]
            game_server_void.add_player(player)
            massage = {"response": {"server_game": {"ip": game_server_void.ip, "port": game_server_void.port}},
                       "type_request": "add_list"}
        elif len(list_player.get_one_player_game_server()) > 0:
            game_server_one_player = list_player.get_one_player_game_server()[0]
            game_server_one_player.add_player(player)
            massage = {"response": {"server_game": {"ip": game_server_one_player.ip, "port": game_server_one_player.port}},
                       "type_request": "add_list"}
        return massage
