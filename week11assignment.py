from dataclasses import dataclass, field
from contextlib import contextmanager

class GradeError(Exception):
    pass

@dataclass
class Student:
    name: str
    scores: list
    _status: str = field(default="PENDING", init=False)

    def __post_init__(self):
        for s in self.scores:
            if s < 0 or s > 100:
                raise GradeError(f"Invalid score for {self.name}")

    @property
    def average(self):
        return round(sum(self.scores) / len(self.scores), 1)

    def __str__(self):
        return f"{self.name}: avg={self.average} [{self._status}]"

    def __gt__(self, other):
        return self.average > other.average

class GradeEvaluator:
    def __init__(self, students, threshold):
        self.students = students
        self.threshold = threshold
        self._cursor = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._cursor >= len(self.students):
            raise StopIteration
        st = self.students[self._cursor]
        if st.average >= self.threshold:
            st._status = "PASSED"
        else:
            st._status = "FAILED"

        self._cursor += 1
        return st

def grade_report(evaluator):
    p = 0
    f = 0

    for st in evaluator:
        if st._status == "PASSED":
            p += 1
        else:
            f += 1

        yield str(st)

    yield f"Total: {p} passed, {f} failed"

@contextmanager
def grading_session(name):
    roster = []
    print(f">>> Session: {name}")
    try:
        yield roster
    except GradeError as e:
        print(f"!!! Error: {e}")
    finally:
        print(f"<<< Closed: {name} ({len(roster)} students)")

with grading_session("Midterm") as roster:
    roster.append(Student("Alice", [85, 90, 78]))
    roster.append(Student("Bob", [55, 60, 45]))
    roster.append(Student("Carol", [92, 88, 95]))

    for line in grade_report(GradeEvaluator(roster, 60)):
        print(line)

    print(roster[0] > roster[1])

print()

with grading_session("Final") as roster:
    roster.append(Student("Eve", [-5, 80, 90]))
