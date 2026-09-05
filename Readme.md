# Python Works

A collection of Python coursework, algorithm implementations, and small console projects. This repo brings together standalone scripts, algorithm exercises, and a couple of small full applications built for BSCS coursework.

## Requirements

- Python 3.9+ (some projects tested up to 3.14)
- No third-party libraries required — everything runs on the standard library

## Projects

### Applications

| Project | Description | Run |
|---|---|---|
| [`advanced_calculator/`](advanced_calculator) | Console calculator with SQLite-backed calculation history (add, search, view, delete). Parses expressions safely with Python's `ast` module instead of raw `eval()`. Supports trig, logs, factorials, constants, and more. Built with a model/controller/database structure. | `python main.py` |
| [`CBR_BOM/`](CBR_BOM) | Console app demonstrating two algorithms: Case-Based Reasoning (retrieve/reuse/revise/retain using Jaccard similarity) and Boyer-Moore string search (bad-character heuristic, with match counting and highlighting). | `python main.py` |
| [`Bank Account Management/`](Bank%20Account%20Management) | Simple bank account system — create accounts, deposit, withdraw, and check balance — via a console menu. | `python BankMain.py` |
| [`SimpleCalculator/`](SimpleCalculator) | Basic four-function calculator (add, subtract, multiply, divide) as a console script. | `python simple_calculator.py` |
| [`GWA Calculator/`](GWA%20Calculator) | Computes a Grade Weighted Average from a list of subjects, grades, and units. | `python GWA_Calculator.py` |

### Algorithms & Data Structures

| Project | Description |
|---|---|
| [`Knacksack_Algorithm/`](Knacksack_Algorithm) | 0/1 Knapsack problem solved with dynamic programming; `knacksack_input.py` runs it interactively and prints the DP table. |
| [`Decrease_and_Conquer/`](Decrease_and_Conquer) | Recursive solution to the Josephus Problem (last-survivor elimination puzzle) using the decrease-and-conquer technique. |
| [`Python_Comparison_BruteForce_x_Dynamic/`](Python_Comparison_BruteForce_x_Dynamic) | Side-by-side brute-force vs. dynamic-programming implementations for two classic problems: regex-style pattern matching (`isMatch`) and the "trapping rain water" problem — used to compare approach and complexity. |
| [`Kleen_Star_Closure/`](Kleen_Star_Closure) | Simulates the Kleene Star closure property on a finite automaton (adds a new start/accept state and epsilon-transitions). Includes a companion PDF (`Closure_Properties_Simulator.pdf`) explaining the theory. |

### Archives

- `MidtermPortfolio.zip` / `Python-SchoolWorks.zip` — bundled coursework submissions.

## Getting Started

Clone the repo:

```bash
git clone https://github.com/KBJOwen29/Python-Works.git
cd Python-Works
```

Then move into whichever project you want and run its entry-point script, e.g.:

```bash
cd advanced_calculator
python main.py
```

## Notes

- These are individual, mostly self-contained projects rather than one unified application — each folder can be run on its own.
- A couple of projects (`advanced_calculator`, `CBR_BOM`) have their own README with more detail on features and structure.

## License

No license specified yet.
