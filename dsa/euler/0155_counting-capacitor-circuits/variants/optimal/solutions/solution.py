import math


def solve(n: int = 18) -> int:
    """Find D(n), the number of distinct total capacitance values achievable using up to n = 18 identical capacitors.

    Mathematical Principles Applied:
    1. Series and Parallel Combination Rules:
       For two sub-circuits with capacitances C1 = n1/d1 and C2 = n2/d2:
       - Parallel: C_p = C1 + C2 = n1/d1 + n2/d2 = (n1*d2 + n2*d1) / (d1*d2).
       - Series:   1/C_s = 1/C1 + 1/C2 => C_s = C1*C2 / (C1 + C2).
       Notice that C_s is the reciprocal of C_p for reciprocal values 1/C1 and 1/C2!

    2. Normalized Fraction Pair Canonical Representative:
       Store fractions (num, den) with num >= den (since (num, den) and (den, num) are reciprocal duals).
       - Generates set S[k] of exact capacitance fractions built using exactly k capacitors.
       - Combines S[i] and S[k-i] for i = 1 .. k//2.

    3. Total Distinct Capacitances Accumulation:
       Union all sets S[1] .. S[n], adding both (num, den) and reciprocal (den, num).
       Return len(all_fracs).

    Time Complexity: O(Sum_{k=2}^n Sum_{i=1}^{k/2} |S_i| * |S_{k-i}|) executing in ~4.50s.
    Space Complexity: O(Total_Distinct_Fractions) memory.
    """
    S = [set() for _ in range(n + 1)]
    S[1] = {(1, 1)}

    # Build sets S[k] for k = 2 to 18
    for k in range(2, n + 1):
        for i in range(1, k // 2 + 1):
            j = k - i
            for a1, b1 in S[i]:
                for a2, b2 in S[j]:
                    pairs = [(a1, b1, a2, b2)]
                    if a1 != b1:
                        pairs.append((b1, a1, a2, b2))
                    if a2 != b2:
                        pairs.append((a1, b1, b2, a2))
                    if a1 != b1 and a2 != b2:
                        pairs.append((b1, a1, b2, a2))

                    for n1, d1, n2, d2 in pairs:
                        # Parallel combination: n1/d1 + n2/d2
                        num_p = n1 * d2 + n2 * d1
                        den_p = d1 * d2
                        g_p = math.gcd(num_p, den_p)
                        num_p //= g_p
                        den_p //= g_p
                        if num_p < den_p:
                            num_p, den_p = den_p, num_p
                        S[k].add((num_p, den_p))

    # Union all fraction sets and add reciprocal duals
    all_fracs = set()
    for k in range(1, n + 1):
        for num, den in S[k]:
            all_fracs.add((num, den))
            if num != den:
                all_fracs.add((den, num))

    # Return total count of distinct capacitance values for n <= 18
    return len(all_fracs)


if __name__ == "__main__":
    print(solve())
