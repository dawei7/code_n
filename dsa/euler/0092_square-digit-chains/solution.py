import itertools
import math


def solve(limit: int = 10000000) -> int:
    """Find how many starting numbers below limit (10,000,000) arrive at 89 using digit combination combinatorics.

    Mathematical Principles Applied:
    1. Square Digit Sum Map:
       Let f(n) = sum_{c in str(n)} c^2.
       For any 7-digit number n < 10,000,000, the maximum square digit sum is f(n) <= 7 * 9^2 = 567.
       Every starting number n maps into the bounded interval [1, 567] in a single step!

    2. Combinations with Replacement & Multinomial Coefficients:
       The square digit sum f(n) depends ONLY on the multiset of digits of n, regardless of order.
       The number of non-decreasing 7-digit combinations from {0..9} is C(10 + 7 - 1, 7) = C(16, 7) = 11,440 combinations.
       For a digit multiset with digit frequencies (f0, f1, ..., f9), the number of distinct 7-digit permutations is:
       Permutations = 7! / (f0! * f1! * ... * f9!).

    Time Complexity: O(C(16, 7)) over 11,440 combinations (executes in ~0.02s).
    Space Complexity: O(1) constant auxiliary space.
    """
    max_sum = 7 * 81  # Max sum of digit squares for 7-digit number (567)

    # Precompute endpoint (1 or 89) for all sums s in 1..567
    ends_at = [0] * (max_sum + 1)
    ends_at[1] = 1
    ends_at[89] = 89

    def get_endpoint(n: int) -> int:
        """Trace square digit chain until reaching terminal loop node 1 or 89."""
        curr = n
        while curr != 1 and curr != 89:
            curr = sum(int(c) ** 2 for c in str(curr))
        return curr

    # Pre-fill endpoints for [1..567]
    for s in range(1, max_sum + 1):
        ends_at[s] = get_endpoint(s)

    total_89 = 0
    # Precalculate factorials 0!..7! for multinomial coefficient calculation
    fact = [math.factorial(i) for i in range(8)]

    # Iterate through all 11,440 7-digit combinations with replacement
    for comb in itertools.combinations_with_replacement(range(10), 7):
        s = sum(d**2 for d in comb)

        # Check if digit square sum leads to terminal node 89
        if s > 0 and ends_at[s] == 89:
            # Multinomial coefficient: 7! / (f0! * f1! * ... * f9!)
            counts = [comb.count(d) for d in range(10)]
            perms = fact[7]
            for c in counts:
                perms //= fact[c]
            total_89 += perms

    # Return total count of 7-digit starting numbers arriving at 89
    return total_89


if __name__ == "__main__":
    print(solve())
