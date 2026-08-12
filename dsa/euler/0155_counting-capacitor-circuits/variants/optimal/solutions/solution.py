import math


def solve(n: int = 18) -> int:
    """Find D(n), the number of distinct total capacitance values achievable using up to n capacitors.
    
    Time Complexity: O(Sum_{k=2}^n Sum_{i=1}^{k/2} |S_i| * |S_{k-i}|)
    Space Complexity: O(Total_Distinct_Fractions)
    """
    S = [set() for _ in range(n + 1)]
    S[1] = {(1, 1)}

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
                        # Parallel addition: n1/d1 + n2/d2 = (n1*d2 + n2*d1) / (d1*d2)
                        num_p = n1 * d2 + n2 * d1
                        den_p = d1 * d2
                        g_p = math.gcd(num_p, den_p)
                        num_p //= g_p
                        den_p //= g_p
                        if num_p < den_p:
                            num_p, den_p = den_p, num_p
                        S[k].add((num_p, den_p))

    all_fracs = set()
    for k in range(1, n + 1):
        for num, den in S[k]:
            all_fracs.add((num, den))
            if num != den:
                all_fracs.add((den, num))

    return len(all_fracs)
