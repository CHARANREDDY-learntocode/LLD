from server.model.question import Question
from server.model.commentable import Comment
from server.model.votable import Vote
from server.model.tag import Tag


class QuestionService:
    def __init__(self, session):
        self.session = session

    def add_question(self, author, content):
        id_ = len(self.session.get_docs("Question"))
        question = Question(id_, author, content)
        self.session.add_doc("Question", question, id_)
        author.add_question(question)
        return question

    def search_question(self, query):
        results = []
        for question in self.session.get_docs("Question"):
            if query in question.content or query in question.tags:
                results.append(question)
        return results

    def add_comment(self, question, author, content):
        id_ = len(self.session.get_docs("Comment")) + 1
        comment = Comment(id_, author, content)
        question.add_comment(comment)
        self.session.add_doc("Comment", comment, id_)
        author.add_comment(comment)

    def add_tag(self, question, tag_name):
        id_ = len(self.session.get_docs("Tag")) + 1
        tag = Tag(id_, tag_name)
        self.session.add_doc("Tag", tag, id_)
        question.add_tag(tag)

    @staticmethod
    def add_vote(question, author, value):
        vote = Vote(author, value)
        question.register_vote(vote)

