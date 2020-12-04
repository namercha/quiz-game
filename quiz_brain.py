class QuizBrain:

    def __init__(self, questions_list):
        self.questions_list = questions_list
        self.question_number = 0

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        input(f"Q.{self.question_number}: {current_question.text} (True/False) ")