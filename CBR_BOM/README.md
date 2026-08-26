# CBR & BOM Algorithm Application

A beginner-friendly Python console application demonstrating:

1. **CBR - Case-Based Reasoning**
2. **BOM - Boyer-Moore String Search**

## Requirements

- Python 3.9 or newer
- No external libraries are required.

## Project Structure

```text
cbr_bom_application/
├── model/
│   ├── case.py
│   └── search_result.py
├── controller/
│   ├── cbr_controller.py
│   └── bom_controller.py
├── data/
│   └── cases.json
├── main.py
├── testing_main.py
└── README.md
```

## Running the Application

Open a terminal inside the project directory:

```bash
python main.py
```

## Running Tests

```bash
python testing_main.py
```

## CBR

The CBR module follows the basic Case-Based Reasoning process:

**Retrieve → Reuse → Revise → Retain**

The current implementation focuses on retrieving the most similar previous case using Jaccard word similarity and recommending its solution. When a new case is added, it is retained in `data/cases.json`.

## BOM

The BOM module implements the Boyer-Moore string-search algorithm using the **Bad Character Heuristic**.

It can:

- Search for a pattern
- Find multiple occurrences
- Display the bad-character table
- Count character comparisons
- Count shifts
- Highlight matches

## Notes

The project intentionally uses only Python's standard library so it can be easily submitted, demonstrated, and modified for school requirements.
