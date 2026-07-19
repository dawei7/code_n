def solve(rolls: list[int], mean: int, n: int) -> list[int]:
    missing_sum = mean * (len(rolls) + n) - sum(rolls)
    if missing_sum < n or missing_sum > 6 * n:
        return []

    quotient, remainder = divmod(missing_sum, n)
    return [quotient + 1] * remainder + [quotient] * (n - remainder)
