from abc import ABC, abstractmethod


class Votable(ABC):
    @abstractmethod
    def register_vote(self, vote):
        pass


class Vote:
    def __init__(self, user, value):
        self.__user = user
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, updated_value):
        self.__value = updated_value
