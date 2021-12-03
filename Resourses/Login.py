from Models import User
from ClassServer import StartApplication as app
from Interfase.Response import Response
from ClassServer.Models_json.LoginMassega import LoginMessage


class Login(Response):

    @classmethod
    def post(cls, message):
        args = cls.parser_message(message, LoginMessage)
        user_database = app().context.query(User).filter(User.email == args.email).first()
        if user_database and user_database.check_password(args.password):
            return {"response": {"id": user_database.id,
                                 "email": user_database.email,
                                 "nickname": user_database.nickname,
                                 "password": user_database.password},
                    "type_request": "login"}
        else:
            return {"response": {"type_error": "LoginOut",
                                 "massage_error": "Неправильный логин или пароль"}}
