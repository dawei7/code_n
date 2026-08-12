def fib(n: int) -> int:
    """Compute n-th Fibonacci number."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def solve(target_k: int = 15) -> int:
    """Find target_k-th Fibonacci Golden Nugget n = F_(2k) * F_(2k+1).
    
    Time Complexity: O(k)
    Space Complexity: O(1)
    """
    f_2k = fib(2 * target_k)
    f_2k1 = fib(2 * target_k + 1)
    return f_2k * f_2k1
