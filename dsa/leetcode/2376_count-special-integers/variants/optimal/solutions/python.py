from __future__ import annotations


def solve(n: int) -> int:
    def permutations(available: int, slots: int) -> int:
        result = 1
        for offset in range(slots):
            result *= available - offset
        return result

    digits = str(n)
    length = len(digits)
    answer = 0

    for shorter_length in range(1, length):
        answer += 9 * permutations(9, shorter_length - 1)

    used: set[int] = set()
    for index, char in enumerate(digits):
        current = int(char)
        first_candidate = 1 if index == 0 else 0
        remaining_slots = length - index - 1

        for candidate in range(first_candidate, current):
            if candidate not in used:
                answer += permutations(
                    10 - (index + 1),
                    remaining_slots,
                )

        if current in used:
            break
        used.add(current)
    else:
        answer += 1

    return answer
