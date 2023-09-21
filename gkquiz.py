class question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

class quiz:
    def __init__(self):
        self.questions = []
        self.score = 0
        self.current_question_index =0

    def add_question(self, text, answer):
        new_question = question(text, answer)
        self.questions.append(new_question)

    def next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question.text
        else:
            return None

    def check_answer(self, user_answer):
        if self.current_question_index <= len(self.questions):
            
            question = self.questions[self.current_question_index - 1]
            if user_answer.lower() == question.answer.lower():
                self.score += 2
            else:
                self.score -= 1

    def do_questions_remain(self):
        return self.current_question_index < len(self.questions)

    def start_quiz(self):
        print("Welcome to True or False Trivia by GDSC")
        while self.do_questions_remain():
            question_text = self.next_question()
            if question_text is not None:
                user_answer = input(f"{question_text} (True/False): ").strip()
                self.check_answer(user_answer)

        print(f"Thank you for participating. Your score is: {self.score}")


# creating a quiz object
quiz1 = quiz()

# Adding questions to the quiz
quiz1.add_question("A slug's blood is green.", "True")
quiz1.add_question("The loudest animal is the African Elephant.", "False")
quiz1.add_question("Approximately one quarter of human bones are in the feet.", "True")
quiz1.add_question("The total surface area of a human lungs is the size of a football pitch.", "True")
quiz1.add_question("In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "True")
quiz1.add_question("In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "False")
quiz1.add_question("It is illegal to pee in the Ocean in Portugal.", "True")
quiz1.add_question("You can lead a cow down stairs but not up stairs.", "False")
quiz1.add_question("Google was originally called 'Backrub'.", "True")
quiz1.add_question("Buzz Aldrin's mother's maiden name was 'Moon'.", "True")
quiz1.add_question("No piece of square dry paper can be folded in half more than 7 times.", "False")
quiz1.add_question("A few ounces of chocolate can to kill a small dog.", "True")


#to start the quiz
quiz1.start_quiz()
