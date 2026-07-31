def solve(n: int, m: int) -> int:
    divisible_count = n // m
    return (
        n * (n + 1) // 2
        - m * divisible_count * (divisible_count + 1)
    )
