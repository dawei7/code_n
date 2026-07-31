from __future__ import annotations


def solve(pattern: str) -> str:
    answer: list[str] = []
    pending: list[str] = []
    n = len(pattern)

    for digit in range(1, n + 2):
        pending.append(str(digit))
        if digit == n + 1 or pattern[digit - 1] == "I":
            while pending:
                answer.append(pending.pop())

    return "".join(answer)
