def solve(n: int, k: int) -> int:
    return sum(value for value in range(max(1, n - k), n + k + 1) if n & value == 0)
