from server.model.user import User


class UserService:
    def __init__(self, session):
        self.__session = session

    def create_user(self, name, email):
        id_ = len(self.__session.get_docs("User")) + 1
        user = User(id_, name, email)
        self.__session.add_doc("User", user, id_)
        return user

    @staticmethod
    def get_questions_by_user(user):
        return user.get_questions()



