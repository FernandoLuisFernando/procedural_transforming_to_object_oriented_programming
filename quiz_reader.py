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
    
class quiz:
    def __init__(self, filename):
        self.filename = filename
        self.questions = []

    def load_questions(self): 
        with open(self.filename, "r") as file:
            content = file.read()

        blocks = content.strip().split("---\n")

        for block in blocks:
            lines = block.strip().split("\n")
            if len(lines) < 6:
                continue

            q_text = lines[0].split(':')[1].strip()  
            option_a = lines[1][3:].strip()
            option_b = lines[2][3:].strip()
            option_c = lines[3][3:].strip()
            option_d = lines[4][3:].strip()
            correct_answer = lines[5].split(':')[1].strip()

            options = = {"a": option_a, "b": option_b, "c": option_c, "d": option_d}
            question = Question(q_text, options, correct_answer)
            self.questions.append(question)

    def start_quiz(self):
        selected_questions = random.sample(self.questions, min(3, len (self.questions)))

        for idx, question in enumerate(selected_questions, start=1):
            print(f"\nQuestion {idx}")
            question.display()
            
        