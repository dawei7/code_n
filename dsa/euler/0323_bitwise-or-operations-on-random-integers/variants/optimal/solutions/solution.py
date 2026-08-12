def solve(bits: int = 32, decimals: int = 10) -> str:
    """Find the expected number of steps N for bitwise-OR of random 32-bit integers to reach 2^32 - 1.
    
    Time Complexity: O(k_max) via Tail Probability Infinite Summation
    Space Complexity: O(1)
    """
    E_N = 0.0
    for k in range(0, 100):
        p_le_k = (1.0 - 0.5**k) ** bits
        E_N += 1.0 - p_le_k
    return f"{E_N:.{decimals}f}"
