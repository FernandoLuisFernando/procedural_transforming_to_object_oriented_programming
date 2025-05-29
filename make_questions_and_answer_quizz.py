class questions:
    def __init__(self, number, text, option_a, option_b, option_c, option_d, correct_answer):
        self.number = number
        self.text = text
        self.option_a = option_a
        self.option_b = option_b
        self.option_c = option_c
        self.option_d = option_d
        self.answer = correct_answer

    def format(self):
        return (f"question {self.number}: {self.text}\n"
                f"a) {self.option_a}\n"
                f"b) {self.option_b}\n"
                f"c) {self.option_c}\n"
                f"d) {self.option_d}\n"            
                f"Correct Answer: {self.answer}\n"
                "---\n ")
    
class Quiz:
    def __init__(self):
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def create_questions(self):
        for num in range (1, 4):
            print(f"\n--- Question {num} ---")
            text = input("Enter the question text: ")
            option_a = input("Enter option A: ")
            option_b = input("Enter option B: ")
            option_c = input("Enter option C: ")
            option_d = input("Enter option D: ")

            correct_answer = ""
            while correct_answer not in ["a", "b", "c", "d"]:
                correct_answer = input("Enter the correct answer: (a,b,c,d)").lower()
                if correct_answer not in ["a", "b", "c", "d"]:
                    print("Invalid input. Please enter a, b, c, or d.")
                
            final = questions(questions, text, option_a, option_b, option_c, option_d, correct_answer)
            self.add_question(final)

    def save_files(self, filename):
            with open(filename, 'w') as file:
                for question in self.questions:
                    file.write(question.format())  
            print(f"Quiz saved to {filename}")

quiz_final = Quiz()
Quiz.create_questions(self=quiz_final)
quiz_final.save_files("quiz.txt")
   

             