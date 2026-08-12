def solve(consecutive: int = 4, target_factors: int = 4) -> int:
    """Find the first of consecutive integers to each have target_factors distinct prime factors.
    
    Time Complexity: O(N log log N)
    Space Complexity: O(N)
    """
    limit = 200000
    factors = [0] * limit

    for i in range(2, limit):
        if factors[i] == 0:  # i is prime
            for j in range(i, limit, i):
                factors[j] += 1

    count = 0
    for i in range(2, limit):
        if factors[i] == target_factors:
            count += 1
            if count == consecutive:
                return i - consecutive + 1
        else:
            count = 0

    return -1
