def solve(limit: int = 10**12) -> int:
    """Find the number of odd-triplets [n, k, f(n, k)] with n <= limit.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Odd Subset Sum Parity f(n, k):
       f(n, k) is the number of k-element subsets of {1, ..., n} with an odd sum.
       An odd-triplet requires n, k, and f(n, k) all to be odd.

    2. Combinatorial Parity Reduction & Lucas' Theorem:
       - Parity analysis over binomial coefficients shows f(n, k) is odd iff
         n = 4m + 1 and k = 2j + 1 where j is a bitwise submask of m (j AND m == j).
       - For each m, the number of valid j is exactly 2^{popcount(m)}.
       - Thus, the total number of odd-triplets for n <= limit is:
           S(M) = sum_{m=0}^{M} 2^{popcount(m)},   where M = floor((limit - 1) / 4).

    3. Logarithmic Digit DP Evaluation:
       In binary representation, each bit b_i = 1 can either be 0 (contributing 3^{rem_len}
       since each remaining position can be 0 or 1 with weight 1 or 2, sum = 1+2 = 3)
       or 1 (carrying a factor of 2).
       This evaluates in O(log(limit)) operations.

    Complexity:
    -----------
    - Time Complexity: O(log(limit)) (< 0.0001 seconds).
    - Space Complexity: O(1) auxiliary space.
    """
    if limit < 1:
        return 0

    M = (limit - 1) // 4
    if M < 0:
        return 0

    ans = 0
    ones_so_far = 0
    bits = [int(b) for b in bin(M)[2:]]
    length = len(bits)

    for idx, bit in enumerate(bits):
        if bit == 1:
            remaining_len = length - 1 - idx
            ans += (2**ones_so_far) * (3**remaining_len)
            ones_so_far += 1

    ans += 2**ones_so_far
    return ans


if __name__ == "__main__":
    print(solve())
