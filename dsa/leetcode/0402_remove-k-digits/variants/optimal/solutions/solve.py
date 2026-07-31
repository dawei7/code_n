"""Optimal app-local solution for LeetCode 402: Remove K Digits."""


def solve(num: str, k: int) -> str:
    stack: list[str] = []
    remaining = k

    for digit in num:
        while remaining and stack and stack[-1] > digit:
            stack.pop()
            remaining -= 1
        stack.append(digit)

    if remaining:
        del stack[-remaining:]

    normalized = "".join(stack).lstrip("0")
    return normalized or "0"
