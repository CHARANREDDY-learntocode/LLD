from service.question import QuestionService
from service.answer import AnswerService
from service.user import UserService
from server.db.session import Session


class StackOverFlowDemo:
    def __init__(self):
        self.session = Session()

    def create_user(self, name, email):
        service = UserService(self.session)
        return service.create_user(name, email)

    def create_question(self, author, content):
        service = QuestionService(self.session)
        return service.add_question(author, content)

    def create_answer(self, question, author, content):
        service = AnswerService(self.session)
        return service.add_answer(question, author, content)

    def add_comment_to_question(self, question, author, content):
        service = QuestionService(self.session)
        return service.add_comment(question, author, content)

    def add_comment_to_answer(self, answer, author, content):
        service = AnswerService(self.session)
        return service.add_comment(answer, author, content)

    def add_vote_to_question(self, question, author, value):
        return QuestionService(self.session).add_vote(question, author, value)

    def add_vote_to_answer(self, answer, author, value):
        return AnswerService(self.session).add_vote(answer, author, value)

    def add_tag_to_question(self, question, tag_name):
        return QuestionService(self.session).add_tag(question, tag_name)

    def search_questions(self, query):
        return QuestionService(self.session).search_question(query)

    def get_questions_by_user(self, user):
        return UserService(self.session).get_questions_by_user(user)


demo = StackOverFlowDemo()

charan = demo.create_user("Charan", "charan@example.com")
jyoti = demo.create_user("Jyoti", "jyothi@example.com")
dosth = demo.create_user("Dosthgiri", "dosth@example.com")

demo.create_question(charan, "Inheritance - Multiple & Multi level")
demo.create_question(jyoti, "Abstraction")

print(demo.get_questions_by_user(charan))
print(demo.get_questions_by_user(jyoti))
print(demo.session.get_docs("Question"))