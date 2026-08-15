from math import factorial


def solve(target_idx: int = 150000) -> int:
    """Find the target_idx-th integer n for which phi(n) = 13! = 6,227,020,800.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Inverse Totient Problem:
       We seek integers n where phi(n) = 13! = 2^10 * 3^5 * 5^2 * 7 * 11 * 13 = 6,227,020,800.
       For n = 2^a * prod_{i} p_i^{k_i}, Euler's totient is:
           phi(n) = phi(2^a) * prod_{i} (p_i - 1) * p_i^{k_i - 1}.

    2. Candidate Prime Divisors:
       For every odd prime p dividing n, (p - 1) MUST divide 13!.
       - We compute all divisors d of 13!.
       - If d + 1 is prime, then p = d + 1 is a valid candidate prime factor.

    3. Depth-First Search Backtracking:
       Branching on choices of prime powers (p_i - 1) * p_i^{k_i - 1} dividing the remaining
       totient target, we collect all 182,752 solutions in sorted order.

    Complexity:
    -----------
    - Time Complexity: O(divisors(13!) + DFS) (~0.55 seconds).
    - Space Complexity: O(total_solutions) storage (< 15 MB).
    """
    target_phi = factorial(13)
    phi_factors = {2: 10, 3: 5, 5: 2, 7: 1, 11: 1, 13: 1}

    divs = [1]
    for p, count in phi_factors.items():
        next_divs = []
        p_pow = 1
        for _ in range(count + 1):
            for div in divs:
                next_divs.append(div * p_pow)
            p_pow *= p
        divs = next_divs

    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        d = 5
        while d * d <= n:
            if n % d == 0 or n % (d + 2) == 0:
                return False
            d += 6
        return True

    valid_odd_primes = [d + 1 for d in divs if d + 1 > 2 and is_prime(d + 1)]
    valid_odd_primes.sort(reverse=True)

    prime_options = []
    for p in valid_odd_primes:
        opts = []
        phi_val = p - 1
        val_n = p
        while target_phi % phi_val == 0:
            opts.append((phi_val, val_n))
            val_n *= p
            phi_val *= p
        prime_options.append(opts)

    pow2_opts = []
    a = 2
    phi_val = 2 ** (a - 1)
    val_n = 2**a
    while target_phi % phi_val == 0:
        pow2_opts.append((phi_val, val_n))
        a += 1
        phi_val = 2 ** (a - 1)
        val_n = 2**a

    all_solutions = set()

    def dfs(idx: int, curr_phi_rem: int, curr_n: int) -> None:
        if curr_phi_rem == 1:
            all_solutions.add(curr_n)
            all_solutions.add(curr_n * 2)
            return

        if idx >= len(valid_odd_primes):
            for p_val, v_n in pow2_opts:
                if curr_phi_rem == p_val:
                    all_solutions.add(curr_n * v_n)
            return

        p_opts = prime_options[idx]
        for phi_val, val_n in p_opts:
            if curr_phi_rem % phi_val == 0:
                dfs(idx + 1, curr_phi_rem // phi_val, curr_n * val_n)

        dfs(idx + 1, curr_phi_rem, curr_n)

    dfs(0, target_phi, 1)

    sols = sorted(list(all_solutions))
    return sols[target_idx - 1]


if __name__ == "__main__":
    print(solve())
