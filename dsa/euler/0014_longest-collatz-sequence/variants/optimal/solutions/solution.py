def solve(limit: int = 1000000) -> int:
    """Find the starting number under limit with the longest Collatz sequence.
    
    Time Complexity: O(limit)
    Space Complexity: O(limit)
    """
    memo = {1: 1}

    def get_length(n: int) -> int:
        if n in memo:
            return memo[n]
        if n % 2 == 0:
            length = 1 + get_length(n // 2)
        else:
            length = 1 + get_length(3 * n + 1)
        memo[n] = length
        return length

    max_len = 0
    best_start = 1
    # Only test starting numbers in the upper half [limit // 2, limit]
    for i in range(limit // 2, limit):
        length = get_length(i)
        if length > max_len:
            max_len = length
            best_start = i

    return best_start
