"""Candidate with conventional position naming for LeetCode 293: Flip Game."""


def solve(currentState: str) -> list[str]:
    return [
        currentState[:i] + "--" + currentState[i + 2 :]
        for i in range(len(currentState) - 1)
        if currentState[i : i + 2] == "++"
    ]
