class Calculation:
    def __init__(self, expression, result, calculation_id=None, created_at=None):
        self.id = calculation_id
        self.expression = expression
        self.result = result
        self.created_at = created_at

    def to_dict(self):
        return {
            "id": self.id,
            "expression": self.expression,
            "result": self.result,
            "created_at": self.created_at,
        }
