from constant import ReputationConstant
from error.exceptions import InvalidReputationValue


class User:
    def __init__(self, id_, name, email):
        self.__id = id_
        self.__name = name
        self.__email = email
        self.__reputation = 0
        self.__comments = []
        self.__questions = []
        self.__answers = []

    def update_reputation(self, value):
        if value not in ReputationConstant.VALID_VALUES:
            raise InvalidReputationValue()
        self.__reputation += value

    def add_comment(self, comment):
        self.update_reputation(1)
        self.__comments.append(comment)

    def add_question(self, question):
        self.update_reputation(1)
        self.__questions.append(question)

    def add_answer(self, answer):
        self.update_reputation(1)
        self.__answers.append(answer)

    def get_questions(self):
        return self.__questions


