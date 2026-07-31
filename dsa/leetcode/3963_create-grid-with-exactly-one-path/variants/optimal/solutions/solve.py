def solve(m: int, n: int) -> list[str]:
    return ["." * n] + ["#" * (n - 1) + "." for _ in range(m - 1)]
