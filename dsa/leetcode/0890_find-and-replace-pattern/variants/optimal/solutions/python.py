"""Optimal app-local solution for LeetCode 890."""


def solve(words, pattern):
    def signature(text):
        identifiers = {}
        return tuple(
            identifiers.setdefault(character, len(identifiers))
            for character in text
        )

    target = signature(pattern)
    return [word for word in words if signature(word) == target]
