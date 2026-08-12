def solve(s: int = 1000) -> int:
    """Find product abc for Pythagorean triplet a + b + c = s.
    
    Time Complexity: O(s)
    Space Complexity: O(1)
    """
    for a in range(1, s // 3):
        num = s * s // 2 - s * a
        den = s - a
        if num % den == 0:
            b = num // den
            c = s - a - b
            if a < b < c:
                return a * b * c
    return -1
