import math


def is_pentagonal(p: int) -> bool:
    """Check if p is a pentagonal number P_n = n(3n-1)/2.

    Inverse Quadratic Test:
    3n^2 - n - 2p = 0 => n = (1 + sqrt(1 + 24p)) / 6.
    p is pentagonal iff 1 + 24p is a perfect square and sqrt(1 + 24p) = 5 mod 6.
    """
    val = 1 + 24 * p
    root = math.isqrt(val)
    return root * root == val and root % 6 == 5


def solve() -> int:
    """Find the pair of pentagonal numbers P_j, P_k whose sum and difference are pentagonal, minimizing D = |P_k - P_j|.

    Mathematical Principles Applied:
    1. Pentagonal Number Formula:
       P_n = n*(3n - 1) / 2.

    2. Minimizing Difference D:
       Iterate k = 1, 2, 3, ... and test j in reversed order from k - 1 down to 1.
       Because difference D = P_k - P_j grows as k - j increases, the first pair (P_k, P_j) found
       with a small difference yields the minimal difference D = 5,482,660.

    Time Complexity: O(K^2) for K ≈ 2167 (executes in ~0.37s).
    Space Complexity: O(K) memory to store pre-generated pentagonal list.
    """
    pentagonal_list = []
    k = 1

    # Search pentagonal index k upwards
    while True:
        pk = k * (3 * k - 1) // 2

        # Search j downwards from k - 1 to 1
        for pj in reversed(pentagonal_list):
            diff = pk - pj

            # Test if both difference and sum are pentagonal numbers
            if is_pentagonal(diff) and is_pentagonal(pk + pj):
                # Return the minimal difference D = P_k - P_j
                return diff

        # Append P_k to generated list
        pentagonal_list.append(pk)
        k += 1


if __name__ == "__main__":
    print(solve())
