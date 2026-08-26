import json
import os
import re
from model.case import Case


class CBRController:
    """Controller for Case-Based Reasoning."""

    def __init__(self, data_file):
        self.data_file = data_file
        self.cases = []
        self.load_cases()

    def load_cases(self):
        if not os.path.exists(self.data_file):
            self.cases = []
            return

        with open(self.data_file, "r", encoding="utf-8") as file:
            data = json.load(file)

        self.cases = [Case.from_dict(item) for item in data]

    def save_cases(self):
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)

        with open(self.data_file, "w", encoding="utf-8") as file:
            json.dump(
                [case.to_dict() for case in self.cases],
                file,
                indent=4,
                ensure_ascii=False
            )

    @staticmethod
    def tokenize(text):
        return set(re.findall(r"[a-zA-Z0-9]+", text.lower()))

    def calculate_similarity(self, problem, case):
        """Jaccard similarity based on words/keywords."""
        problem_words = self.tokenize(problem)
        case_words = self.tokenize(
            case.problem + " " + " ".join(case.keywords)
        )

        if not problem_words or not case_words:
            return 0.0

        intersection = problem_words & case_words
        union = problem_words | case_words

        return len(intersection) / len(union)

    def retrieve(self, problem, top_n=3):
        results = []

        for case in self.cases:
            score = self.calculate_similarity(problem, case)
            results.append((case, score))

        results.sort(key=lambda item: item[1], reverse=True)
        return results[:top_n]

    def add_case(self, problem, solution, keywords=None):
        next_id = max((case.case_id for case in self.cases), default=0) + 1

        new_case = Case(
            next_id,
            problem.strip(),
            solution.strip(),
            keywords or []
        )

        self.cases.append(new_case)
        self.save_cases()
        return new_case

    def get_case(self, case_id):
        for case in self.cases:
            if case.case_id == case_id:
                return case
        return None

    def list_cases(self):
        return self.cases

    def solve(self, problem):
        """Retrieve the most similar case and return its recommendation."""
        results = self.retrieve(problem, top_n=1)

        if not results:
            return None, 0.0

        case, score = results[0]
        return case, score
