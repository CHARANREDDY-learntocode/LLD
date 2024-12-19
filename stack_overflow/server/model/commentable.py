from abc import ABC, abstractmethod


class Commentable(ABC):
    @abstractmethod
    def add_comment(self, comment):
        pass


class Comment:
    def __init__(self, id_, author, content):
        self._id = id_
        self.__author = author
        self.__content = content

    @property
    def author(self):
        return self.__author

    @property
    def content(self):
        return self.__content
    
    @content.setter
    def content(self, value):
        self.__content = value

