def solve(limit: int = 28123) -> int:
    """Find the sum of all integers up to limit that cannot be written as the sum of two abundant numbers.
    
    Time Complexity: O(N log N + K^2)
    Space Complexity: O(N)
    """
    div_sum = [0] * (limit + 1)
    for i in range(1, limit + 1):
        for j in range(2 * i, limit + 1, i):
            div_sum[j] += i

    abundants = [i for i in range(12, limit + 1) if div_sum[i] > i]
    is_abundant_sum = [False] * (limit + 1)

    for i in range(len(abundants)):
        for j in range(i, len(abundants)):
            s = abundants[i] + abundants[j]
            if s <= limit:
                is_abundant_sum[s] = True
            else:
                break

    return sum(i for i in range(1, limit + 1) if not is_abundant_sum[i])
