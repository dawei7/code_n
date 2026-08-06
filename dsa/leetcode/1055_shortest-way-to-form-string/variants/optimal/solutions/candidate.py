"""Optimal solution for LeetCode 1055: Shortest Way to Form String."""


def solve(source: str, target: str) -> int:
    source_length = len(source)
    next_position = [[-1] * 26 for _ in range(source_length + 1)]

    for source_position in range(source_length - 1, -1, -1):
        next_position[source_position] = next_position[source_position + 1][:]
        next_position[source_position][ord(source[source_position]) - ord("a")] = source_position

    subsequences = 1
    source_index = 0

    for character in target:
        letter = ord(character) - ord("a")
        position = next_position[source_index][letter]
        if position < 0:
            subsequences += 1
            position = next_position[0][letter]
            if position < 0:
                return -1
        source_index = position + 1

    return subsequences
