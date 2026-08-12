PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


def solve(target_solutions: int = 4000000) -> int:
    """Find least n for which number of distinct solutions to 1/x + 1/y = 1/n exceeds 4,000,000.
    
    Time Complexity: O(Exponent Vectors)
    Space Complexity: O(1)
    """
    target_d_n2 = 2 * target_solutions - 1
    best_n = float('inf')

    def dfs(prime_idx: int, max_exp: int, current_n: int, current_d_n2: int):
        nonlocal best_n

        if current_d_n2 > target_d_n2:
            if current_n < best_n:
                best_n = current_n
            return

        if prime_idx >= len(PRIMES):
            return

        p = PRIMES[prime_idx]

        for e in range(1, max_exp + 1):
            next_n = current_n * (p**e)
            if next_n >= best_n:
                break
            next_d = current_d_n2 * (2 * e + 1)
            dfs(prime_idx + 1, e, next_n, next_d)

    dfs(0, 15, 1, 1)

    return best_n
