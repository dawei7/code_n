"""Optimal app-local solution for LeetCode 1023."""


def solve(queries, pattern):
    def matches(query):
        pattern_index = 0
        for character in query:
            if pattern_index < len(pattern) and character == pattern[pattern_index]:
                pattern_index += 1
            elif character.isupper():
                return False
        return pattern_index == len(pattern)

    return [matches(query) for query in queries]
