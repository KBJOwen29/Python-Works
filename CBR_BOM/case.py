class Case:
    """Represents a previous problem/solution case for CBR."""

    def __init__(self, case_id, problem, solution, keywords=None):
        self.case_id = case_id
        self.problem = problem
        self.solution = solution
        self.keywords = keywords or []

    def to_dict(self):
        return {
            "case_id": self.case_id,
            "problem": self.problem,
            "solution": self.solution,
            "keywords": self.keywords
        }

    @staticmethod
    def from_dict(data):
        return Case(
            data["case_id"],
            data["problem"],
            data["solution"],
            data.get("keywords", [])
        )

    def __str__(self):
        return (
            f"Case ID: {self.case_id}\n"
            f"Problem: {self.problem}\n"
            f"Solution: {self.solution}\n"
            f"Keywords: {', '.join(self.keywords)}"
        )
