import math


def solve(n: int = 10**12) -> str:
    """Find u_n + u_{n+1} for n = 10^12 formatted to 9 decimal places.
    
    Time Complexity: O(1) - stabilizes in < 1000 iterations.
    Space Complexity: O(1)
    """
    def f(x):
        val = 2**(30.403243784 - x * x)
        return math.floor(val) * 1e-9

    u = -1.0
    for _ in range(1000):
        u = f(u)

    u_next = f(u)
    ans = u + u_next
    return f"{ans:.9f}"
