from .commentable import Commentable
from .votable import Votable


class Question(Commentable, Votable):
    def __init__(self, id_, author, content):
        self.__id = id_
        self.__author = author
        self.__content = content
        self.__tags = set()
        self.__answers = []
        self.__comments = []
        self.__votes = {}

    def __repr__(self):
        return self.__content

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content):
        self.__content = content

    def add_tag(self, tag):
        self.__tags.add(tag)

    @property
    def tags(self):
        return self.__tags

    def add_answer(self, answer):
        self.__answers.append(answer)

    def add_comment(self, comment):
        self.__comments.append(comment)

    def register_vote(self, vote):
        self.__votes[vote.user] = vote


