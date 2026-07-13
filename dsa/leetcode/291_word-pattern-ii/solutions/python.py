"""Optimal backtracking solution for LeetCode 291: Word Pattern II."""


def solve(pattern: str, s: str) -> bool:
    assignment: dict[str, str] = {}
    used: set[str] = set()

    def search(pattern_index: int, string_index: int) -> bool:
        if pattern_index == len(pattern):
            return string_index == len(s)
        if string_index == len(s):
            return False

        symbol = pattern[pattern_index]
        if symbol in assignment:
            value = assignment[symbol]
            return s.startswith(value, string_index) and search(
                pattern_index + 1,
                string_index + len(value),
            )

        minimum_suffix = sum(
            len(assignment[future]) if future in assignment else 1
            for future in pattern[pattern_index + 1 :]
        )
        latest_end = len(s) - minimum_suffix
        for end in range(string_index + 1, latest_end + 1):
            candidate = s[string_index:end]
            if candidate in used:
                continue
            assignment[symbol] = candidate
            used.add(candidate)
            if search(pattern_index + 1, end):
                return True
            used.remove(candidate)
            del assignment[symbol]
        return False

    return search(0, 0)
