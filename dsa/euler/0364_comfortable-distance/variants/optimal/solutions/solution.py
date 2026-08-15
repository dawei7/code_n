"""Project Euler Problem 364: Comfortable Distance.

Find T(1000000) mod 100000007, where T(N) is the number of valid seating orders for N people.
"""


def solve(n: int = 1000000, mod: int = 100000007) -> int:
    """Compute T(n) mod 100000007 using 3-phase combinatorial partition."""
    if n <= 0:
        return 0
    if n == 1:
        return 1

    # Precompute factorials and modular inverses up to n + 5
    max_fact = n + 5
    fact = [1] * (max_fact + 1)
    inv = [1] * (max_fact + 1)
    for i in range(1, max_fact + 1):
        fact[i] = (fact[i - 1] * i) % mod
    inv[max_fact] = pow(fact[max_fact], mod - 2, mod)
    for i in range(max_fact - 1, -1, -1):
        inv[i] = (inv[i + 1] * (i + 1)) % mod

    def n_cr(n_val: int, r_val: int) -> int:
        if r_val < 0 or r_val > n_val:
            return 0
        return (fact[n_val] * inv[r_val] % mod) * inv[n_val - r_val] % mod

    # Precompute powers of 2 modulo mod
    pow2 = [1] * (n + 5)
    for i in range(1, len(pow2)):
        pow2[i] = (pow2[i - 1] * 2) % mod

    total = 0
    # Iterate over boundary gap sizes L in {0, 1} and R in {0, 1}
    for left_gap in (0, 1):
        for right_gap in (0, 1):
            rem = n - 1 - left_gap - right_gap
            if rem < 0:
                continue

            # 2*a + 3*b = rem
            max_b = rem // 3
            for b in range(0, max_b + 1):
                if (rem - 3 * b) % 2 == 0:
                    a = (rem - 3 * b) // 2
                    k = a + b + 1

                    ways_arrange = n_cr(a + b, b)
                    ways_phase1 = fact[k]
                    ways_phase2 = (
                        pow2[b] * fact[b + left_gap + right_gap]
                    ) % mod
                    ways_phase3 = fact[a + b]

                    term = ways_arrange * ways_phase1 % mod
                    term = term * ways_phase2 % mod
                    term = term * ways_phase3 % mod

                    total = (total + term) % mod

    return total


if __name__ == "__main__":
    print(solve())
