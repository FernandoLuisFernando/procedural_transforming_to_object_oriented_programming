import random

class question:
    def __init__(self, text, options, correct_answer):
        self.text = text 
        self.options = options 
        self.correct_answer = correct_answer

    def display(self):
        print(f"      {self.text}")
        for key, value in self.optionsitems():
            print(f"      {key}) {value}") 

    def check_answer(self, user_answer):
        return user_answer == self.correct_answer
      