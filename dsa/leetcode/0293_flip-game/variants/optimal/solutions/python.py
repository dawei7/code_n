"""Optimal output-sensitive solution for LeetCode 293: Flip Game."""


def solve(currentState: str) -> list[str]:
    return [
        currentState[:index] + "--" + currentState[index + 2 :]
        for index in range(len(currentState) - 1)
        if currentState[index : index + 2] == "++"
    ]
