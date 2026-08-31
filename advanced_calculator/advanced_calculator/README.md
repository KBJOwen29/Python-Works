# Advanced Python Calculator

A console-based advanced calculator built with Python and SQLite local storage.

## Features

- Addition, subtraction, multiplication, division
- Floor division and modulo
- Exponentiation
- Square root
- Factorial
- Absolute value
- Sine, cosine, tangent
- Natural logarithm and base-10 logarithm
- Exponential, ceiling, floor
- Degree/radian conversion
- Constants: pi, e, tau
- Parentheses
- Safe expression evaluation using Python's `ast` module
- SQLite local calculation history
- Search history
- View individual calculations
- Delete individual calculations
- Clear history
- Separate testing file
- Model / Controller / Database architecture

## Requirements

Python 3.9 or newer is recommended.

No external packages are required.

## Run

From the project folder:

```bash
python main.py
```

The SQLite database will automatically be created as:

```text
calculator.db
```

## Run tests

```bash
python testing/testing_main.py
```

## Project Structure

```text
advanced_calculator/
│
├── main.py
├── README.md
├── calculator.db              # created automatically after running
│
├── model/
│   ├── calculation.py
│   └── history.py
│
├── controller/
│   ├── calculator_controller.py
│   └── history_controller.py
│
├── database/
│   └── database.py
│
└── testing/
    └── testing_main.py
```

## Example Expressions

```text
10 + 5
25 * 4
100 / 4
2 ** 10
sqrt(144)
factorial(5)
sin(30)
cos(60)
tan(45)
log(10)
log10(1000)
pi * 10 ** 2
(50 + 25) / 5
```

## Security

The calculator does not use raw `eval()`.

Expressions are parsed using Python's `ast` module, and only explicitly approved operators, functions, constants, and numeric values are accepted.
