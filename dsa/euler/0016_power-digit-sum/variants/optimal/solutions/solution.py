def solve(exp: int = 1000) -> int:
    """Find the sum of digits of 2^exp.
    
    Time Complexity: O(exp)
    Space Complexity: O(exp)
    """
    return sum(int(d) for d in str(2**exp))
