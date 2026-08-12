def solve(expansions: int = 1000) -> int:
    """In the first 1000 expansions of sqrt(2), count fractions with len(numerator) > len(denominator).
    
    Time Complexity: O(expansions)
    Space Complexity: O(1)
    """
    n, d = 3, 2
    count = 0

    for _ in range(expansions):
        if len(str(n)) > len(str(d)):
            count += 1
        n, d = n + 2 * d, n + d

    return count
