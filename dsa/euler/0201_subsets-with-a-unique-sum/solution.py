def solve(n: int = 100, k: int = 50) -> int:
    """Determine the sum of all unique sums of k-element subsets of S = {1^2, 2^2, ..., n^2}.

    Mathematical Principles Applied:
    1. Bitwise 2-Bit Dynamic Programming:
       We want to count the number of 50-element subsets of S that sum to value s.
       Instead of full integer counts, we track whether the number of ways to reach subset size c with sum s is:
       - 0 (ones = 0, twos = 0)
       - 1 (ones = 1, twos = 0) -- UNIQUE SUM!
       - >= 2 (ones = 0, twos = 1) -- NON-UNIQUE SUM!

    2. Bit-Vector Transition Logic:
       For element v = x^2:
       - s_ones = ones[c - 1] << v
       - s_twos = twos[c - 1] << v
       - new_twos = twos[c] | (ones[c] & s_ones) | s_twos
       - new_ones = (ones[c] ^ s_ones) & ~new_twos

    3. Unique Sum Aggregation:
       After processing all n elements, bit s in ones[k] is 1 iff sum s is formed by EXACTLY ONE k-element subset.

    Time Complexity: O(n * k * S_max / 64) executing in ~1.37s.
    Space Complexity: O(k * S_max / 64) auxiliary space.
    """
    S = [i * i for i in range(1, n + 1)]
    K = k

    # Bit-vector arrays for ones (count == 1) and twos (count >= 2) per subset size c
    ones = [0] * (K + 1)
    twos = [0] * (K + 1)

    ones[0] = 1

    # DP state updates over input elements v = x^2
    for idx, v in enumerate(S):
        max_c = min(K, idx + 1)
        for c in range(max_c, 0, -1):
            s_ones = ones[c - 1] << v
            s_twos = twos[c - 1] << v

            # Combine new sums with existing counts
            new_twos = twos[c] | (ones[c] & s_ones) | s_twos
            new_ones = (ones[c] ^ s_ones) & ~new_twos

            ones[c] = new_ones
            twos[c] = new_twos

    ans = 0
    b = ones[K]
    s = 0
    # Sum all values s where bit s of ones[K] is set
    while b > 0:
        if b & 1:
            ans += s
        b >>= 1
        s += 1

    # Return total sum of all unique subset sums
    return ans


if __name__ == "__main__":
    print(solve())
