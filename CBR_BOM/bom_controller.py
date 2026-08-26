from model.search_result import SearchResult


class BOMController:
    """
    Boyer-Moore string-search controller.

    Uses the Bad Character Heuristic.
    """

    @staticmethod
    def build_bad_character_table(pattern):
        table = {}

        # The last occurrence of each character is stored.
        for index, character in enumerate(pattern):
            table[character] = index

        return table

    def search(self, text, pattern):
        if pattern == "":
            return SearchResult(pattern, text, [0], 0, 0)

        if len(pattern) > len(text):
            return SearchResult(pattern, text, [], 0, 0)

        bad_character = self.build_bad_character_table(pattern)

        positions = []
        comparisons = 0
        shifts = 0

        m = len(pattern)
        n = len(text)
        shift = 0

        while shift <= n - m:
            j = m - 1

            while j >= 0:
                comparisons += 1

                if pattern[j] == text[shift + j]:
                    j -= 1
                else:
                    break

            if j < 0:
                positions.append(shift)

                # Continue searching for overlapping matches.
                if shift + m < n:
                    next_char = text[shift + m]
                    last_occurrence = bad_character.get(next_char, -1)
                    amount = max(1, m - last_occurrence)
                else:
                    amount = 1
            else:
                mismatched_char = text[shift + j]
                last_occurrence = bad_character.get(mismatched_char, -1)
                amount = max(1, j - last_occurrence)

            shift += amount
            shifts += 1

        return SearchResult(
            pattern,
            text,
            positions,
            comparisons,
            shifts
        )

    @staticmethod
    def highlight_matches(text, pattern, positions):
        """Returns text with matches surrounded by [ ]."""
        if not positions or not pattern:
            return text

        result = []
        last_index = 0
        pattern_length = len(pattern)

        for position in positions:
            if position < last_index:
                continue

            result.append(text[last_index:position])
            result.append("[")
            result.append(text[position:position + pattern_length])
            result.append("]")
            last_index = position + pattern_length

        result.append(text[last_index:])
        return "".join(result)
