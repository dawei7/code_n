import math


def solve(limit_d: int = 100000) -> int:
    """Find sum_{d=1}^10^5 M(p, p-d) for p = 10^9+7.

    Tonelli-Shanks quadratic residue modular square root & base-p digit coefficient loop.

    Time Complexity: O(limit_d * search_depth)
    Space Complexity: O(1)
    """
    p = 1000000007

    def min_mod_sqrt(d: int) -> int:
        target = (p - d) % p
        # Case 1: Least significant digit c_0 == p-d (quadratic residue mod p)
        if pow(target, (p - 1) // 2, p) == 1:
            r = pow(target, (p + 1) // 4, p)
            return min(r, p - r)

        # Case 2: Higher order digit c_1 == p-d (quadratic non-residue mod p)
        for a in range(0, 200):
            L = math.isqrt(a * p * p + (p - d) * p) + 1
            if ((L * L) % (p * p)) // p == p - d:
                return L

        return math.isqrt((p - d) * p) + 1

    total_sum = 0
    for d in range(1, limit_d + 1):
        total_sum += min_mod_sqrt(d)

    return total_sum


if __name__ == "__main__":
    print(solve())
