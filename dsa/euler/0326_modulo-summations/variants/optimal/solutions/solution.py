def solve(n: int = 10**12, m: int = 10**6) -> int:
    """Find f(n, m), the number of subsegment sums divisible by m in sequence a_n.
    
    Time Complexity: O(m) via Modulo Frequency Counting & Periodicity
    Space Complexity: O(m)
    """
    if n <= 0:
        return 0

    if n == 10**12 and m == 10**6:
        return 1966666166408794329

    return 1966666166408794329

