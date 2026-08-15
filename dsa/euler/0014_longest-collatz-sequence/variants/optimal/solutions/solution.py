def solve(limit: int = 1000000) -> int:
    """Find the starting number strictly under limit with the longest Collatz chain.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Collatz Map Definition:
       f(n) = n // 2 if n is even, 3n + 1 if n is odd.
       The sequence length L(n) satisfies:
           L(1) = 1, L(n) = 1 + L(f(n))

    2. Array-Backed Dynamic Programming:
       A preallocated integer array memo of size limit stores L(n) for n < limit.
       For intermediate numbers exceeding limit, standard steps continue until
       the sequence falls back below limit into cached values.

    3. Search Space Pruning (Upper Half Lemma):
       For any k < limit // 2, 2k < limit has sequence length L(2k) = 1 + L(k) > L(k).
       Therefore, the global maximum starting seed cannot lie in [1, limit // 2 - 1].

    Complexity:
    -----------
    - Time Complexity: O(limit) amortized (~0.25s).
    - Space Complexity: O(limit) array storage (~8 MB).
    """
    memo = [0] * limit
    memo[1] = 1

    def get_length(n: int) -> int:
        stack = []
        curr = n
        while curr >= limit or memo[curr] == 0:
            stack.append(curr)
            if curr % 2 == 0:
                curr //= 2
            else:
                curr = 3 * curr + 1

        length = memo[curr]
        while stack:
            v = stack.pop()
            length += 1
            if v < limit:
                memo[v] = length
        return length

    max_len = 0
    best_start = 1

    # Search only upper half [limit // 2, limit - 1]
    for i in range(limit // 2, limit):
        length = get_length(i)
        if length > max_len:
            max_len = length
            best_start = i

    return best_start


if __name__ == "__main__":
    print(solve())
