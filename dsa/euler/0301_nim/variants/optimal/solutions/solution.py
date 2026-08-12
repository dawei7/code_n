def solve(k: int = 30) -> int:
    """Find the number of 1 <= n <= 2^30 for which n ^ 2n ^ 3n == 0.
    
    Time Complexity: O(k) via Fibonacci Sequence
    Space Complexity: O(k)
    """
    fib = [0, 1]
    for _ in range(k + 2):
        fib.append(fib[-1] + fib[-2])
    return fib[k + 2]
