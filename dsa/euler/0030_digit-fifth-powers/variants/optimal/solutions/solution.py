def solve(power: int = 5) -> int:
    """Find sum of all numbers equal to the sum of fifth powers of their digits.
    
    Time Complexity: O(limit * log10(limit))
    Space Complexity: O(1)
    """
    powers = [d**power for d in range(10)]
    limit = 6 * (9**power)  # Upper bound 354294
    
    total = 0
    for i in range(10, limit + 1):
        if i == sum(powers[int(c)] for c in str(i)):
            total += i
    return total
