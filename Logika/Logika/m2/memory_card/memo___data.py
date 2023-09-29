from PyQt5.QtCore import QAbstractListModel, QModelIndex, Qt
from random import randint, shuffle

class Question():
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3


    def got_right(self):
        print("це правельна відповідь!")

    def got_right(self):
        print("відповідь невірна")

class QuestionView():
    def __init__(self, frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
            self.frm_model = frm_model
            self.question
            self.answer = answer
            self.wrong_answer1 = wrong_answer1
            self.wrong_answer2 = wrong_answer2
            self.wrong_answer3 = wrong_answer3

    def show(self):
        self.question.setText(self.frm_model.question)
        self.question.setText(self.frm_model.aswer)
        self.answer.setText(self.frm_model.wrong_answer1)
        self.answer.setText(self.frm_model.wrong_answer2)
        self.answer.setText(self.frm_model.wrong_answer3)


