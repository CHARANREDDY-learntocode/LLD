from .commentable import Commentable
from .votable import Votable


class Answer(Commentable, Votable):
    def __init__(self, id_, question, author, content, is_accepted=False):
        self.__id = id_
        self.__question = question
        self.__author = author
        self.__content = content
        self.__comments = []
        self.__votes = {}
        self.__is_accepted = is_accepted

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content):
        self.__content = content

    @property
    def is_accepted(self):
        return self.__is_accepted

    @is_accepted.setter
    def is_accepted(self, value):
        self.__is_accepted = value

    @property
    def question(self):
        return self.__question

    def add_comment(self, comment):
        self.__comments.append(comment)

    def register_vote(self, vote):
        self.__votes[vote.user] = vote


