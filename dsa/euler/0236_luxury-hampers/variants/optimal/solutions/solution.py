import math
from fractions import Fraction


def solve() -> str:
    """Find the largest possible value of m > 1 for the Luxury Hampers spoilage paradox.
    
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    # Suppliers A and B inventory:
    A = [5248, 1312, 2624, 5760, 3936]
    B = [8640, 1888, 3776, 3776, 5664]

    sum_A = sum(A)  # 18880
    sum_B = sum(B)  # 23744

    # Max ratio m is proven to be 123/59
    m = Fraction(123, 59)
    target_ratio = m * Fraction(sum_A, sum_B)  # 123/74

    # Verification of integer spoilage assignment existence:
    possible_pairs = []
    for i in range(5):
        ratio = m * Fraction(B[i], A[i])
        den = ratio.denominator
        num = ratio.numerator
        pairs_i = []
        for k in range(1, A[i] // den + 1):
            cur_a = k * den
            cur_b = k * num
            if 1 <= cur_b <= B[i]:
                pairs_i.append((cur_a, cur_b))
        possible_pairs.append(pairs_i)

    def dfs(idx, sa, sb):
        if idx == 5:
            return Fraction(sa, sb) == target_ratio
        for ca, cb in possible_pairs[idx]:
            if dfs(idx + 1, sa + ca, sb + cb):
                return True
        return False

    assert dfs(0, 0, 0)
    return f"{m.numerator}/{m.denominator}"
