from collections import defaultdict


class Session:
    def __init__(self):
        self.__data = defaultdict(dict)

    def add_doc(self, table, doc, id_):
        self.__data[table][id_] = doc

    def get_docs(self, table):
        return self.__data[table]
