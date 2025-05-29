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
                f"Correct An swer: {self.correct_answer}\n"
                "---\n ")
    
    class quiz:
        def __init__(self):
            self.questions = []

        def add_question(self, question):
            self.question.append(question)

        def craete_questions(self):
            for questions in range(1, 4):
                print(f"\n--- Question {questions} ---")
                text = input("Enter the question text: ")
                option_a = input("Enter option A: ")
                option_b = input("Enter option B: ")
                option_c = input("Enter option C: ")
                option_d = input("Enter option D: ")

                


   

             