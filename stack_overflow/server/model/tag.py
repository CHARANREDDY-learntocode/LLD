"""
This module handles tags

It includes classes for:
- Tag management

Classes:
    - Tag: Manages Tag
"""


class Tag:
    def __init__(self, _id, name):
        self.__id = _id
        self.__name = name

    @property
    def name(self):
        return self.__name

    @property
    def id_(self):
        return self.__id
