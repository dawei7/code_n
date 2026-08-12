import math
import itertools


def solve(limit: int = 10000000) -> int:
    """Find how many starting numbers below limit arrive at 89 using digit combination combinatorics.
    
    Time Complexity: O(C(10+7-1, 7)) = O(11440)
    Space Complexity: O(1)
    """
    # 1. Precompute endpoints for sums up to 7 * 9^2 = 567
    max_sum = 7 * 81
    ends_at = [0] * (max_sum + 1)
    ends_at[1] = 1
    ends_at[89] = 89

    def get_endpoint(n: int) -> int:
        curr = n
        while curr != 1 and curr != 89:
            curr = sum(int(c)**2 for c in str(curr))
        return curr

    for s in range(1, max_sum + 1):
        ends_at[s] = get_endpoint(s)

    # 2. Count numbers via digit combinations of length 7
    total_89 = 0
    fact = [math.factorial(i) for i in range(8)]

    for comb in itertools.combinations_with_replacement(range(10), 7):
        s = sum(d**2 for d in comb)
        if s > 0 and ends_at[s] == 89:
            # Multinomial coefficient: 7! / (f0! f1! ... f9!)
            counts = [comb.count(d) for d in range(10)]
            perms = fact[7]
            for c in counts:
                perms //= fact[c]
            total_89 += perms

    return total_89
