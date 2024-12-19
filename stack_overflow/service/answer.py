from server.model.answer import Answer
from server.model.commentable import Comment
from server.model.votable import Vote


class AnswerService:
    def __init__(self, session):
        self.__session = session

    @property
    def session(self):
        return self.__session

    def add_answer(self, question, author, content, is_accepted=False):
        id_ = len(self.session.get_docs("Answer")) + 1
        answer = Answer(id_, question, author, content, is_accepted=is_accepted)
        self.session.add_doc("Answer", answer, id_)
        author.add_answer(answer)
        return answer

    def add_comment(self, answer, author, content):
        id_ = len(self.session.get_docs("Comment")) + 1
        comment = Comment(id_, author, content)
        answer.add_comment(comment)
        self.session.add_doc("Comment", comment, id_)
        author.add_comment(comment)

    @staticmethod
    def add_tag(answer, tag):
        answer.add_tag(tag)

    @staticmethod
    def add_vote(answer, author, value):
        vote = Vote(author, value)
        answer.register_vote(vote)