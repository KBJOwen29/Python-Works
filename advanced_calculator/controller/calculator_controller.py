import ast
import math
import operator

import database.database as Database


class SafeCalculator:
    BINARY_OPERATORS = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.FloorDiv: operator.floordiv,
        ast.Mod: operator.mod,
        ast.Pow: operator.pow,
    }

    UNARY_OPERATORS = {
        ast.UAdd: operator.pos,
        ast.USub: operator.neg,
    }

    FUNCTIONS = {
        "sqrt": math.sqrt,
        "factorial": math.factorial,
        "abs": abs,
        "sin": lambda x: math.sin(math.radians(x)),
        "cos": lambda x: math.cos(math.radians(x)),
        "tan": lambda x: math.tan(math.radians(x)),
        "log": math.log,
        "ln": math.log,
        "log10": math.log10,
        "exp": math.exp,
        "ceil": math.ceil,
        "floor": math.floor,
        "degrees": math.degrees,
        "radians": math.radians,
    }

    CONSTANTS = {
        "pi": math.pi,
        "e": math.e,
        "tau": math.tau,
    }

    def evaluate(self, expression):
        if len(expression) > 500:
            raise ValueError("Expression is too long.")

        tree = ast.parse(expression, mode="eval")
        return self._evaluate_node(tree.body)

    def _evaluate_node(self, node):
        if isinstance(node, ast.Constant):
            if isinstance(node.value, bool) or not isinstance(node.value, (int, float)):
                raise ValueError("Only numeric values are allowed.")
            return node.value

        if isinstance(node, ast.BinOp):
            operation = self.BINARY_OPERATORS.get(type(node.op))
            if operation is None:
                raise ValueError("Operator is not allowed.")

            left = self._evaluate_node(node.left)
            right = self._evaluate_node(node.right)

            if isinstance(node.op, ast.Pow) and abs(right) > 10000:
                raise ValueError("Exponent is too large.")

            return operation(left, right)

        if isinstance(node, ast.UnaryOp):
            operation = self.UNARY_OPERATORS.get(type(node.op))
            if operation is None:
                raise ValueError("Unary operator is not allowed.")
            return operation(self._evaluate_node(node.operand))

        if isinstance(node, ast.Name):
            if node.id in self.CONSTANTS:
                return self.CONSTANTS[node.id]
            raise ValueError(f"Unknown name: {node.id}")

        if isinstance(node, ast.Call):
            if not isinstance(node.func, ast.Name):
                raise ValueError("Only approved functions are allowed.")

            function = self.FUNCTIONS.get(node.func.id)
            if function is None:
                raise ValueError(f"Unknown function: {node.func.id}")

            if node.keywords:
                raise ValueError("Keyword arguments are not allowed.")

            arguments = [self._evaluate_node(arg) for arg in node.args]

            if node.func.id == "factorial":
                if len(arguments) != 1:
                    raise ValueError("factorial() requires one argument.")
                if not float(arguments[0]).is_integer() or arguments[0] < 0:
                    raise ValueError("factorial() requires a non-negative integer.")
                if arguments[0] > 10000:
                    raise ValueError("Factorial input is too large.")

            return function(*arguments)

        raise ValueError("Invalid expression.")


class CalculatorController:
    def __init__(self):
        self.calculator = SafeCalculator()

    def calculate(self, expression):
        try:
            result = self.calculator.evaluate(expression)
            result = self._format_result(result)
            Database.save_calculation(expression, result)
            return {"success": True, "result": result}
        except ZeroDivisionError:
            return {"success": False, "error": "Cannot divide by zero."}
        except (ValueError, SyntaxError, OverflowError, TypeError, ArithmeticError) as error:
            return {"success": False, "error": str(error) or "Invalid calculation."}

    @staticmethod
    def _format_result(result):
        if isinstance(result, float):
            if not math.isfinite(result):
                raise ValueError("Result is not finite.")
            if result.is_integer():
                return int(result)
            return round(result, 12)
        return result
