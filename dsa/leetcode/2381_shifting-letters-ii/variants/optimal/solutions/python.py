from __future__ import annotations


def solve(s: str, shifts: list[list[int]]) -> str:
    difference = [0] * (len(s) + 1)

    for start, end, direction in shifts:
        amount = 1 if direction == 1 else -1
        difference[start] += amount
        difference[end + 1] -= amount

    answer: list[str] = []
    running_shift = 0
    for index, char in enumerate(s):
        running_shift += difference[index]
        shifted = (ord(char) - ord("a") + running_shift) % 26
        answer.append(chr(ord("a") + shifted))

    return "".join(answer)
