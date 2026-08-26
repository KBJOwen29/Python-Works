import os

from controller.cbr_controller import CBRController
from controller.bom_controller import BOMController


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data", "cases.json")

cbr = CBRController(DATA_FILE)
bom = BOMController()


def pause():
    input("\nPress Enter to continue...")


def print_header(title):
    print("\n" + "=" * 60)
    print(title.center(60))
    print("=" * 60)


def cbr_menu():
    while True:
        print_header("CASE-BASED REASONING (CBR)")
        print("1. Solve a problem")
        print("2. Show top similar cases")
        print("3. Add a new case")
        print("4. View all cases")
        print("0. Back")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            problem = input("\nDescribe your problem: ").strip()

            if not problem:
                print("Problem cannot be empty.")
                pause()
                continue

            case, score = cbr.solve(problem)

            if case is None:
                print("No cases are available.")
            else:
                print("\nMost similar case:")
                print(case)
                print(f"\nSimilarity: {score * 100:.2f}%")

                if score == 0:
                    print("\nNo meaningful similarity was found.")
                elif score >= 0.50:
                    print("Strong match. The previous solution may be useful.")
                elif score >= 0.25:
                    print("Moderate match. Review the solution before applying it.")
                else:
                    print("Weak match. Consider adding a new case.")

            pause()

        elif choice == "2":
            problem = input("\nDescribe the problem: ").strip()

            if not problem:
                print("Problem cannot be empty.")
                pause()
                continue

            results = cbr.retrieve(problem, top_n=3)

            print("\nTop similar cases:")
            for rank, (case, score) in enumerate(results, start=1):
                print(f"\n#{rank} - Similarity: {score * 100:.2f}%")
                print(f"Case {case.case_id}: {case.problem}")
                print(f"Solution: {case.solution}")

            pause()

        elif choice == "3":
            problem = input("\nProblem: ").strip()
            solution = input("Solution: ").strip()
            keyword_input = input("Keywords (comma-separated): ").strip()

            if not problem or not solution:
                print("Problem and solution are required.")
                pause()
                continue

            keywords = [
                keyword.strip()
                for keyword in keyword_input.split(",")
                if keyword.strip()
            ]

            case = cbr.add_case(problem, solution, keywords)
            print(f"\nCase {case.case_id} added successfully.")
            pause()

        elif choice == "4":
            cases = cbr.list_cases()

            if not cases:
                print("\nNo cases found.")
            else:
                for case in cases:
                    print("\n" + "-" * 60)
                    print(case)

            pause()

        elif choice == "0":
            break

        else:
            print("Invalid choice.")
            pause()


def bom_menu():
    while True:
        print_header("BOYER-MOORE (BOM) STRING SEARCH")
        print("1. Search for a pattern")
        print("2. Show bad-character table")
        print("3. Run demonstration")
        print("0. Back")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            text = input("\nEnter text: ")
            pattern = input("Enter pattern: ")

            if not pattern:
                print("Pattern cannot be empty.")
                pause()
                continue

            result = bom.search(text, pattern)

            print("\n" + str(result))

            if result.found:
                highlighted = bom.highlight_matches(
                    text, pattern, result.positions
                )
                print(f"\nHighlighted text:\n{highlighted}")

            pause()

        elif choice == "2":
            pattern = input("\nEnter pattern: ")

            if not pattern:
                print("Pattern cannot be empty.")
                pause()
                continue

            table = bom.build_bad_character_table(pattern)

            print("\nBad-character table:")
            for character, index in table.items():
                display_character = "\\n" if character == "\n" else character
                print(f"'{display_character}' -> {index}")

            pause()

        elif choice == "3":
            text = "The Boyer-Moore algorithm is a fast string searching algorithm."
            pattern = "algorithm"

            result = bom.search(text, pattern)

            print(f"\nText: {text}")
            print(f"Pattern: {pattern}")
            print("\nResult:")
            print(result)

            if result.found:
                print(
                    "\nHighlighted:",
                    bom.highlight_matches(text, pattern, result.positions)
                )

            pause()

        elif choice == "0":
            break

        else:
            print("Invalid choice.")
            pause()


def main():
    while True:
        print_header("CBR & BOM ALGORITHM APPLICATION")
        print("1. Case-Based Reasoning (CBR)")
        print("2. Boyer-Moore String Search (BOM)")
        print("3. About the application")
        print("0. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            cbr_menu()

        elif choice == "2":
            bom_menu()

        elif choice == "3":
            print_header("ABOUT")
            print(
                "This application demonstrates two algorithms:\n\n"
                "CBR - Case-Based Reasoning\n"
                "Uses previous cases to find a similar problem and "
                "recommend its solution.\n\n"
                "BOM - Boyer-Moore\n"
                "Searches for a pattern inside text using the "
                "Bad Character Heuristic."
            )
            pause()

        elif choice == "0":
            print("\nThank you for using the application!")
            break

        else:
            print("Invalid choice.")
            pause()


if __name__ == "__main__":
    main()
