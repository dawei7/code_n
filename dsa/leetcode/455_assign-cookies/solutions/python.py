"""Sorted two-pointer solution for LeetCode 455."""


def solve(g: list[int], s: list[int]) -> int:
    children = sorted(g)
    cookies = sorted(s)
    child = 0
    for cookie in cookies:
        if child < len(children) and cookie >= children[child]:
            child += 1
    return child
