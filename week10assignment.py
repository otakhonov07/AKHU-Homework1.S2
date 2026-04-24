import math

class ExamError(Exception):
    pass

class StudentAlreadyRegisteredError(ExamError):
    def __init__(self, name):
        error_text = ""
        error_text = error_text + "student already registered: "
        error_text = error_text + str(name)
        super().__init__(error_text)
        self.name = name

class StudentNotRegisteredError(ExamError):
    def __init__(self, name):
        error_text = ""
        part1 = "student not registered: "
        error_text = part1 + name
        super().__init__(error_text)
        self.name = name

class InvalidAnswerError(ExamError):
    def __init__(self, question_num, valid_options):
        error_text = "invalid answer for question "
        error_text = error_text + str(question_num)
        error_text = error_text + ". valid options: "
        error_text = error_text + str(valid_options)
        super().__init__(error_text)
        self.question_num = question_num
        self.valid_options = valid_options

class ExamGrader:
    def __init__(self, answer_key):
        self.answerKey = answer_key
        self.submissions = dict()

    def register_student(self, name):
        if name in self.submissions:
            raise StudentAlreadyRegisteredError(name)
        else:
            self.submissions[name] = {}
        return

    def submit_answer(self, name, question_num, answer):
        try:
            student_data = self.submissions[name]
        except:
            raise StudentNotRegisteredError(name) from None

        temp_key = self.answerKey

        if question_num not in temp_key:
            keys_list = []
            for k in temp_key:
                keys_list.append(k)
            raise InvalidAnswerError(question_num, keys_list)

        if name not in self.submissions:
            self.submissions[name] = {}

        self.submissions[name][question_num] = answer

    def grade(self, name):
        try:
            answers = self.submissions[name]
        except:
            raise StudentNotRegisteredError(name) from None

        correct = 0
        total = len(self.answerKey)

        for q in self.answerKey:
            correct_answer = self.answerKey[q]

            if q in answers:
                if answers[q] == correct_answer:
                    correct = correct + 1
                else:
                    pass
            else:
                pass

        if len(answers) == 0:
            return 0

        score = (correct / total) * 100
        final_score = int(score)
        return final_score

key = {1: "B", 2: "A", 3: "C", 4: "D"}
grader = ExamGrader(key)

grader.register_student("Dana")
grader.register_student("Emir")

grader.submit_answer("Dana", 1, "B")
grader.submit_answer("Dana", 2, "A")
grader.submit_answer("Dana", 3, "B")
grader.submit_answer("Dana", 4, "D")

grader.submit_answer("Emir", 1, "B")
grader.submit_answer("Emir", 2, "C")

print(f"Dana: {grader.grade('Dana')}%")
print(f"Emir: {grader.grade('Emir')}%")

tests = [
    lambda: grader.register_student("Dana"),
    lambda: grader.submit_answer("Zara", 1, "A"),
    lambda: grader.submit_answer("Emir", 7, "A"),
]

for t in tests:
    try:
        t()
    except ExamError as e:
        print(e)