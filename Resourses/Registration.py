from Interfase.Response import Response
from Models import User
from ClassServer import StartApplication as app
from ClassServer.Models_json.LoginMassega import LoginMessage


class Registration(Response):

    @classmethod
    def post(cls, message):
        args = cls.parser_message(message, LoginMessage)
        new_user = User(name="lol", sename="lolol", nickname="pop", email=args.email, password=args.password)
        app().context.add(new_user)
        app().context.commit()
        user_database = app().context.query(User).filter(User.email == args.email).first()
        return {"response": {"id": user_database.id,
                             "email": user_database.email,
                             "nickname": user_database.nickname,
                             "password": user_database.password},
                "type_request": "registration"}
