"""
Separate testing file for the CBR and Boyer-Moore implementations.

Run:
    python testing_main.py
"""

import os

from controller.cbr_controller import CBRController
from controller.bom_controller import BOMController


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data", "cases.json")


def test_cbr_similarity():
    cbr = CBRController(DATA_FILE)

    case = cbr.get_case(1)
    assert case is not None

    score = cbr.calculate_similarity(
        "My laptop is slow during startup",
        case
    )

    assert score > 0
    print(f"[PASS] CBR similarity test: {score * 100:.2f}%")


def test_cbr_retrieval():
    cbr = CBRController(DATA_FILE)

    results = cbr.retrieve(
        "My laptop is very slow when starting",
        top_n=3
    )

    assert len(results) > 0
    assert results[0][0].case_id == 1

    print(
        f"[PASS] CBR retrieval test: "
        f"best case = {results[0][0].case_id}"
    )


def test_bom_found():
    bom = BOMController()

    result = bom.search(
        "The quick brown fox jumps over the lazy dog.",
        "brown"
    )

    assert result.positions == [10]
    assert result.found

    print("[PASS] BOM single-match test")


def test_bom_multiple_matches():
    bom = BOMController()

    result = bom.search(
        "banana bandana banana",
        "ana"
    )

    assert result.positions == [1, 3, 11, 16, 18]

    print("[PASS] BOM multiple-match test")


def test_bom_not_found():
    bom = BOMController()

    result = bom.search(
        "hello world",
        "python"
    )

    assert result.positions == []
    assert not result.found

    print("[PASS] BOM not-found test")


def test_bom_bad_character_table():
    bom = BOMController()

    table = bom.build_bad_character_table("banana")

    assert table["a"] == 5
    assert table["n"] == 4
    assert table["b"] == 0

    print("[PASS] BOM bad-character table test")


def run_tests():
    print("=" * 60)
    print("RUNNING CBR & BOM TESTS".center(60))
    print("=" * 60)

    tests = [
        test_cbr_similarity,
        test_cbr_retrieval,
        test_bom_found,
        test_bom_multiple_matches,
        test_bom_not_found,
        test_bom_bad_character_table
    ]

    passed = 0

    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as error:
            print(f"[FAIL] {test.__name__}: {error}")
        except Exception as error:
            print(f"[ERROR] {test.__name__}: {error}")

    print("\n" + "=" * 60)
    print(f"Tests passed: {passed}/{len(tests)}")
    print("=" * 60)

    if passed == len(tests):
        print("All tests passed successfully!")


if __name__ == "__main__":
    run_tests()
