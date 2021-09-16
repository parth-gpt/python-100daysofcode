class QuizBrain:
    def __init__(self, q_list):
        self.q_num = 0
        self.q_list = q_list
        self.score = 0

    def still_have_ques(self):
        if self.q_num < len(self.q_list):  # can also be --> return self.q_num <= len(self.q_list)
            return True
        else:
            return False

    def next_question(self):
        current_question = self.q_list[self.q_num]
        self.q_num += 1
        ans = input(f"Q{self.q_num}: {current_question.text} (True/False)?: ")
        self.check(ans, current_question.answer)

    def check(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's Wrong!")
        print(f"The correct answer was {correct_ans}.")
        print(f"Your current score is {self.score}/{self.q_num}.")
        print("\n")
