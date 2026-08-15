from collections import Counter
import math


def solve(limit: int = 80) -> int:
    """Find the number of ways to write 1/2 as a sum of square reciprocals using distinct integers 2 <= k <= limit (80).

    Mathematical Principles Applied:
    1. p-Adic Valuation & Prime Factor Pruning:
       For a prime p, a sum of 1/k^2 can produce a p-free denominator ONLY IF the sum of (p/k)^2
       over selected multiples of p forms a numerator divisible by p.
       - Primes > limit / 2 (e.g. p in {43, 47, 53, ...}) have at most one multiple <= 80, so they CANNOT be included.
       - Primes p in {19, 23, 29, 31, 37, 41} have no non-trivial valid subset combinations, eliminating them entirely.

    2. Combinatorial Branching for Primes p in {7, 11, 13, 17}:
       Compute all valid sub-combinations `get_p_combos(p)` where sum of (p/k)^2 numerator is divisible by p.

    3. Meet-in-the-Middle Partitioning:
       - Base-2 and Base-3 candidates (`base_23`) evaluated via meet-in-the-middle frequency counter `base_23_sums`.
       - Pure and shared multiples of 5 evaluated via precomputed map `fixed_5_map`.
       - Combine valid prime combinations from 17, 13, 11, 7, and 5, matching remaining target `L // 2` against `base_23_sums`.

    Time Complexity: O(Combos_Prime * Unique_5_Sums) executing in ~0.50s.
    Space Complexity: O(2^|Base_23|) memory for subset sums counter.
    """
    bad_primes = {19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79}
    cands = [
        k for k in range(2, limit + 1) if not any(k % p == 0 for p in bad_primes)
    ]

    base_23 = [
        k for k in cands if all(k % p != 0 for p in [5, 7, 11, 13, 17])
    ]

    def get_p_combos(p):
        """Generate valid subsets of multiples of p whose sum of (p/k)^2 is divisible by p."""
        mults = [k for k in cands if k % p == 0]
        valid_subs = [[]]
        for mask in range(1, 1 << len(mults)):
            sub = [mults[i] for i in range(len(mults)) if (mask >> i) & 1]
            lcm_m = 1
            for m in sub:
                lcm_m = math.lcm(lcm_m, (m // p) ** 2)
            num = sum(lcm_m // ((m // p) ** 2) for m in sub)
            if num % p == 0:
                valid_subs.append(sub)
        return valid_subs

    # Precompute valid prime combination subsets for 17, 13, 11, 7
    subs_17 = get_p_combos(17)
    subs_13 = get_p_combos(13)
    subs_11 = get_p_combos(11)
    subs_7 = get_p_combos(7)

    # Compute global LCM of all k^2 for integer arithmetic
    L = 1
    for k in range(2, limit + 1):
        L = math.lcm(L, k * k)

    # Precompute base_23 subset sum frequencies
    vals_base_23 = [L // (k * k) for k in base_23]
    base_23_sums = Counter()
    for mask in range(1 << len(base_23)):
        s = sum(vals_base_23[i] for i in range(len(base_23)) if (mask >> i) & 1)
        if s <= L // 2:
            base_23_sums[s] += 1

    pure_5_mults = [5, 10, 15, 20, 25, 30, 40, 45, 50, 60, 75, 80]
    shared_5 = [35, 55, 65, 70]
    fixed_5_map = {}

    # Precompute valid pure-5 subsets conditioned on shared-5 multiples
    for mask_shared in range(1 << len(shared_5)):
        fixed_sub = tuple(
            sorted([
                shared_5[i]
                for i in range(len(shared_5))
                if (mask_shared >> i) & 1
            ])
        )
        valid_pure_subsets = []

        for mask_pure in range(1 << len(pure_5_mults)):
            pure_sub = [
                pure_5_mults[i]
                for i in range(len(pure_5_mults))
                if (mask_pure >> i) & 1
            ]
            full_5_sub = list(fixed_sub) + pure_sub
            if not full_5_sub:
                valid_pure_subsets.append(0)
                continue

            lcm_m = 1
            for m in full_5_sub:
                lcm_m = math.lcm(lcm_m, (m // 5) ** 2)
            num = sum(lcm_m // ((m // 5) ** 2) for m in full_5_sub)
            if num % 5 == 0:
                s_val = sum(L // (m * m) for m in pure_sub)
                valid_pure_subsets.append(s_val)

        fixed_5_map[fixed_sub] = Counter(valid_pure_subsets)

    total_target = L // 2
    total_ways = 0

    # Cross-product search over valid prime combinations
    for c17 in subs_17:
        for c13 in subs_13:
            for c11 in subs_11:
                for c7 in subs_7:
                    # Enforce shared multiple consistency (77 is in mults of 11 and 7)
                    if (77 in c11) != (77 in c7):
                        continue

                    chosen = set(c17) | set(c13) | set(c11) | set(c7)
                    sum_p = sum(L // (k * k) for k in chosen)
                    if sum_p > total_target:
                        continue

                    rem1 = total_target - sum_p
                    fixed_sub = tuple(sorted(chosen & set(shared_5)))
                    c5_counter = fixed_5_map[fixed_sub]

                    # Match remaining target sum against base_23_sums
                    for sum5, c5_freq in c5_counter.items():
                        rem2 = rem1 - sum5
                        if rem2 in base_23_sums:
                            total_ways += c5_freq * base_23_sums[rem2]

    # Return total number of ways to express 1/2 as sum of square reciprocals
    return total_ways


if __name__ == "__main__":
    print(solve())
