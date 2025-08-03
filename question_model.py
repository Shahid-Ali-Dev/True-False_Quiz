
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


# from data import question_data
# import random
# score = 0
# que = 1
# game_over = True
# out_of = len(question_data)
# change = len(question_data)-1
# while game_over:
#
#     ran = random.randint(0, change)
#     q = Question(question_data[ran]["text"], question_data[ran]["answer"])
#     guess = input(f"Q.{que} {q.text} (True/False)? ").title()
#     if guess == q.answer:
#         score += 1
#         print(f"Yes you are correct\nYour current score is: {score}/{out_of}")
#         question_data.pop(ran)
#         change -= 1
#         que += 1
#         if score == out_of:
#             print(f"Congratulations on completing the game with all correct answers")
#             game_over = False
#     else:
#         print(f"Sorry you are not correct\nYour final score is {score}/{out_of}")
#         game_over = False