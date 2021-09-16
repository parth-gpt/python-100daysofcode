from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from art import logo

print(logo)
question_bank = []
for ques in question_data:
    new_ques = Question(ques["text"], ques["answer"])
    question_bank.append(new_ques)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_have_ques():
    quiz_brain.next_question()

print("You have completed the quiz!")
print(f"Your final score is - {quiz_brain.score}/{quiz_brain.q_num}.")
