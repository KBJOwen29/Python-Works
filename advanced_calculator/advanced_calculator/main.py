import controller.calculator_controller as CalculatorController
import controller.history_controller as HistoryController
import database.database as Database


def calculate_menu(calc_controller):
    print("\n" + "=" * 50)
    print("                    CALCULATOR")
    print("=" * 50)
    print("Examples:")
    print("  10 + 5")
    print("  25 * 4")
    print("  sqrt(144)")
    print("  sin(30)")
    print("  log(100)")
    print("  2 ** 10")
    print("  (50 + 25) / 5")
    print("\nFunctions: sin, cos, tan, sqrt, log, ln, log10, factorial")
    print("Constants: pi, e")
    print("Type 'back' to return to the main menu.")

    while True:
        expression = input("\nExpression: ").strip()

        if expression.lower() == "back":
            return

        if not expression:
            print("Please enter an expression.")
            continue

        result = calc_controller.calculate(expression)

        if result["success"]:
            print(f"Result: {result['result']}")
            print("Calculation saved to history.")
        else:
            print(f"Error: {result['error']}")


def history_menu(history_controller):
    while True:
        print("\n" + "=" * 50)
        print("                 HISTORY MENU")
        print("=" * 50)
        print("1. View History")
        print("2. Search History")
        print("3. View Calculation")
        print("4. Delete Calculation")
        print("5. Clear History")
        print("6. Back")

        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            records = history_controller.get_all()
            if not records:
                print("\nNo calculation history found.")
            else:
                print("\n" + "-" * 80)
                print(f"{'ID':<5} {'Expression':<35} {'Result':<20} {'Date'}")
                print("-" * 80)
                for r in records:
                    print(f"{r['id']:<5} {r['expression'][:34]:<35} "
                          f"{str(r['result'])[:19]:<20} {r['created_at']}")
                print("-" * 80)

        elif choice == "2":
            term = input("Search expression/result: ").strip()
            records = history_controller.search(term)
            if not records:
                print("No matching calculations found.")
            else:
                for r in records:
                    print(f"\nID: {r['id']}")
                    print(f"Expression: {r['expression']}")
                    print(f"Result: {r['result']}")
                    print(f"Date: {r['created_at']}")

        elif choice == "3":
            try:
                record_id = int(input("Enter calculation ID: "))
                record = history_controller.get_by_id(record_id)
                if record:
                    print("\nCalculation")
                    print(f"ID: {record['id']}")
                    print(f"Expression: {record['expression']}")
                    print(f"Result: {record['result']}")
                    print(f"Date: {record['created_at']}")
                else:
                    print("Calculation not found.")
            except ValueError:
                print("Please enter a valid ID.")

        elif choice == "4":
            try:
                record_id = int(input("Enter calculation ID to delete: "))
                if history_controller.delete(record_id):
                    print("Calculation deleted.")
                else:
                    print("Calculation not found.")
            except ValueError:
                print("Please enter a valid ID.")

        elif choice == "5":
            confirmation = input(
                "Are you sure you want to clear ALL history? (yes/no): "
            ).strip().lower()
            if confirmation == "yes":
                history_controller.clear()
                print("History cleared.")
            else:
                print("Operation cancelled.")

        elif choice == "6":
            return

        else:
            print("Invalid choice.")


def help_menu():
    print("\n" + "=" * 50)
    print("                 CALCULATOR HELP")
    print("=" * 50)
    print("Operators:")
    print("  +   Addition")
    print("  -   Subtraction")
    print("  *   Multiplication")
    print("  /   Division")
    print("  //  Floor division")
    print("  %   Modulo")
    print("  **  Power")
    print("\nFunctions:")
    print("  sqrt(x)       Square root")
    print("  factorial(x)  Factorial")
    print("  abs(x)        Absolute value")
    print("  sin(x)        Sine, degrees")
    print("  cos(x)        Cosine, degrees")
    print("  tan(x)        Tangent, degrees")
    print("  log(x)        Natural logarithm")
    print("  ln(x)         Natural logarithm")
    print("  log10(x)      Base-10 logarithm")
    print("\nConstants:")
    print("  pi")
    print("  e")
    print("\nExamples:")
    print("  sqrt(81) + 10")
    print("  sin(30) * 2")
    print("  factorial(5)")
    print("  log10(1000)")
    print("  (25 + 15) / 4")


def main():
    Database.initialize_database()

    calculator_controller = CalculatorController.CalculatorController()
    history_controller = HistoryController.HistoryController()

    while True:
        print("\n" + "=" * 50)
        print("          ADVANCED PYTHON CALCULATOR")
        print("=" * 50)
        print("1. Calculate")
        print("2. View History")
        print("3. Search History")
        print("4. View Calculation")
        print("5. Delete Calculation")
        print("6. Clear History")
        print("7. Calculator Help")
        print("8. Exit")

        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            calculate_menu(calculator_controller)

        elif choice == "2":
            records = history_controller.get_all()
            if not records:
                print("\nNo calculation history found.")
            else:
                print("\n" + "-" * 80)
                for r in records:
                    print(
                        f"[{r['id']}] {r['expression']} = "
                        f"{r['result']} ({r['created_at']})"
                    )
                print("-" * 80)

        elif choice == "3":
            term = input("Search expression/result: ").strip()
            records = history_controller.search(term)
            if not records:
                print("No matching calculations found.")
            else:
                for r in records:
                    print(
                        f"[{r['id']}] {r['expression']} = "
                        f"{r['result']} ({r['created_at']})"
                    )

        elif choice == "4":
            try:
                record_id = int(input("Enter calculation ID: "))
                record = history_controller.get_by_id(record_id)
                if record:
                    print(f"\nID: {record['id']}")
                    print(f"Expression: {record['expression']}")
                    print(f"Result: {record['result']}")
                    print(f"Date: {record['created_at']}")
                else:
                    print("Calculation not found.")
            except ValueError:
                print("Please enter a valid ID.")

        elif choice == "5":
            try:
                record_id = int(input("Enter calculation ID to delete: "))
                print(
                    "Calculation deleted."
                    if history_controller.delete(record_id)
                    else "Calculation not found."
                )
            except ValueError:
                print("Please enter a valid ID.")

        elif choice == "6":
            confirmation = input(
                "Clear ALL calculation history? (yes/no): "
            ).strip().lower()
            if confirmation == "yes":
                history_controller.clear()
                print("History cleared.")
            else:
                print("Operation cancelled.")

        elif choice == "7":
            help_menu()

        elif choice == "8":
            print("\nThank you for using the Advanced Python Calculator!")
            break

        else:
            print("Invalid choice. Please select 1-8.")


if __name__ == "__main__":
    main()
