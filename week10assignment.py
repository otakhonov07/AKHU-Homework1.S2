import math

class ExamError(Exception):
    pass

class StudentAlreadyRegisteredError(ExamError):
    def __init__(self, name):
        e_txt = ""
        e_txt = e_txt + "student already registered: "
        e_txt = e_txt + str(name)
        super().__init__(e_txt)
        self.name = name

class StudentNotRegisteredError(ExamError):
    def __init__(self, name):
        e_txt = "student not registered: " + name
        super().__init__(e_txt)
        self.name = name

class InvalidAnswerError(ExamError):
    def __init__(self, qn, vo):
        e_txt = "invalid answer for question " + str(qn)
        e_txt = e_txt + ". valid options: " + str(vo)
        super().__init__(e_txt)
        self.qn = qn
        self.vo = vo

class ExamGrader:
    def __init__(self, answer_key):
        self.ans_key = answer_key
        self.db = {}

    def register_student(self, name):
        if name in self.db:
            raise StudentAlreadyRegisteredError(name)
        self.db[name] = {}

    def submit_answer(self, name, question_num, answer):
        try:
            stu_dat = self.db[name]
        except:
            raise StudentNotRegisteredError(name) from None

        ak = self.ans_key

        if question_num not in ak:
            v_list = []
            for k in ak:
                v_list.append(k)
            raise InvalidAnswerError(question_num, v_list)

        if name not in self.db:
            self.db[name] = {}

        self.db[name][question_num] = answer

    def grade(self, name):
        try:
            ans_map = self.db[name]
        except:
            raise StudentNotRegisteredError(name) from None
            
        corr = 0
        tot = len(self.ans_key)

        for q in self.ans_key:
            corr_ans = self.ans_key[q]

            if q in ans_map:
                if ans_map[q] == corr_ans:
                    corr = corr + 1

        if len(ans_map) == 0:
            return 0

        sc = (corr / tot) * 100
        fin_sc = int(sc)
        return fin_sc

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
