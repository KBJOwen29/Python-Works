import controller.calculator_controller as CalculatorController
import controller.history_controller as HistoryController
import database.database as Database


def test_database():
    Database.initialize_database()
    print("[PASS] Database initialization")


def test_calculator():
    controller = CalculatorController.CalculatorController()

    tests = {
        "2 + 3": 5,
        "10 * 5": 50,
        "2 ** 8": 256,
        "sqrt(144)": 12,
        "factorial(5)": 120,
        "sin(30)": 0.5,
        "log10(1000)": 3,
        "pi": 3.141592653590,
        "(25 + 15) / 4": 10,
    }

    for expression, expected in tests.items():
        result = controller.calculate(expression)

        if not result["success"]:
            print(f"[FAIL] {expression}: {result['error']}")
            continue

        actual = result["result"]

        if isinstance(expected, float):
            passed = abs(actual - expected) < 0.000001
        else:
            passed = actual == expected

        print(
            f"[{'PASS' if passed else 'FAIL'}] "
            f"{expression} = {actual}"
        )


def test_security():
    controller = CalculatorController.CalculatorController()

    dangerous_inputs = [
        "__import__('os').system('echo hacked')",
        "open('calculator.db')",
        "eval('2+2')",
    ]

    for expression in dangerous_inputs:
        result = controller.calculate(expression)
        passed = not result["success"]
        print(
            f"[{'PASS' if passed else 'FAIL'}] "
            f"Blocked: {expression}"
        )


def test_history():
    history = HistoryController.HistoryController()
    records = history.get_all()

    print(f"[PASS] History can be read. Records: {len(records)}")

    if records:
        record = history.get_by_id(records[0]["id"])
        if record:
            print("[PASS] Individual history record can be retrieved.")
        else:
            print("[FAIL] Individual history record retrieval.")


def run_tests():
    print("=" * 60)
    print("         ADVANCED CALCULATOR TEST SUITE")
    print("=" * 60)

    test_database()
    test_calculator()
    test_security()
    test_history()

    print("=" * 60)
    print("Testing complete.")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()
