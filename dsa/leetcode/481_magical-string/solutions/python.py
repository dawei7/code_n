"""Two-pointer magical string generation for LeetCode 481."""


def solve(n: int) -> int:
    if n <= 0:
        return 0
    magical = [1, 2, 2]
    read = 2
    next_value = 1
    while len(magical) < n:
        magical.extend([next_value] * magical[read])
        next_value = 3 - next_value
        read += 1
    return magical[:n].count(1)
