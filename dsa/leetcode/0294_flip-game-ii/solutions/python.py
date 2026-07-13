"""Sprague-Grundy solution for LeetCode 294: Flip Game II."""


def solve(currentState: str) -> bool:
    runs: list[int] = []
    run_length = 0
    for symbol in currentState + "-":
        if symbol == "+":
            run_length += 1
        elif run_length:
            runs.append(run_length)
            run_length = 0

    maximum = max(runs, default=0)
    grundy = [0] * (maximum + 1)
    for length in range(2, maximum + 1):
        reachable = {
            grundy[left] ^ grundy[length - left - 2]
            for left in range(length - 1)
        }
        mex = 0
        while mex in reachable:
            mex += 1
        grundy[length] = mex

    position = 0
    for length in runs:
        position ^= grundy[length]
    return position != 0
