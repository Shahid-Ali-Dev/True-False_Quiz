
class Quiz:
    def __init__(self, question_list):

        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    def still_has_question(self):
        return len(self.question_list) > self.question_number


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        guess = input(f"Q.{self.question_number}: {current_question.text} (True/False)? ").title()
        correct_answer = current_question.answer
        self.check_answer(guess, correct_answer)

    def check_answer(self, guess, correct_answer):

        if guess == correct_answer:
            self.score += 1
            print(f"You got it")
        else:
            print(f"Sorry it's wrong")
        print(f"Your current score is {self.score}/{self.question_number}")
        print(f"The correct answer was {correct_answer}")

