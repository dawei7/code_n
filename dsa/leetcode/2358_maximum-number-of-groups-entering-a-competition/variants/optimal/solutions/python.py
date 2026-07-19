import math

def solve(grades: list[int]) -> int:
    n = len(grades)
    # Solve k * (k + 1) / 2 <= n
    # k^2 + k - 2n <= 0
    # k = (-1 + sqrt(1 + 8n)) / 2
    return (-1 + math.isqrt(1 + 8 * n)) // 2
