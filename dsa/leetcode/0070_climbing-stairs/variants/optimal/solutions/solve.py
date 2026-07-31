def solve(n: int) -> int:
    if n <= 2:
        return n
    two_before, one_before = 1, 2
    for _ in range(3, n + 1):
        two_before, one_before = one_before, two_before + one_before
    return one_before
