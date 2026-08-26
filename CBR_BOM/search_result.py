class SearchResult:
    """Stores the result of a Boyer-Moore pattern search."""

    def __init__(self, pattern, text, positions, comparisons, shifts):
        self.pattern = pattern
        self.text = text
        self.positions = positions
        self.comparisons = comparisons
        self.shifts = shifts

    @property
    def found(self):
        return len(self.positions) > 0

    def __str__(self):
        if self.found:
            position_text = ", ".join(map(str, self.positions))
            status = f"Pattern found at index/indices: {position_text}"
        else:
            status = "Pattern was not found."

        return (
            f"{status}\n"
            f"Comparisons: {self.comparisons}\n"
            f"Character shifts: {self.shifts}"
        )
