"""Optimal solution for LeetCode 1023: Camelcase Matching."""


def solve(queries: list[str], pattern: str) -> list[bool]:
    def matches(query: str) -> bool:
        i = 0
        for char in query:
            if i < len(pattern) and char == pattern[i]:
                i += 1
            elif char.isupper():
                return False
        return i == len(pattern)

    return [matches(query) for query in queries]
