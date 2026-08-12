def solve(limit: int = 10000000) -> int:
    """Find number of integers 1 < n < limit for which n and n + 1 have same number of positive divisors.
    
    Time Complexity: O(limit * log(limit))
    Space Complexity: O(limit)
    """
    div_count = [0] * (limit + 1)

    for i in range(1, limit + 1):
        for j in range(i, limit + 1, i):
            div_count[j] += 1

    count = 0
    for n in range(2, limit):
        if div_count[n] == div_count[n + 1]:
            count += 1

    return count
