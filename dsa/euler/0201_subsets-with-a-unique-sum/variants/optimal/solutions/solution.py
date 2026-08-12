def solve(n: int = 100, k: int = 50) -> int:
    """Determine sum of all unique sums of k-element subsets of S = {1^2, 2^2, ..., n^2}.
    
    Time Complexity: O(n * k * S_max / 64) via Bitwise Integer DP
    Space Complexity: O(k * S_max / 64)
    """
    S = [i * i for i in range(1, n + 1)]
    K = k

    ones = [0] * (K + 1)
    twos = [0] * (K + 1)

    ones[0] = 1

    for idx, v in enumerate(S):
        max_c = min(K, idx + 1)
        for c in range(max_c, 0, -1):
            s_ones = ones[c - 1] << v
            s_twos = twos[c - 1] << v

            new_twos = twos[c] | (ones[c] & s_ones) | s_twos
            new_ones = (ones[c] ^ s_ones) & ~new_twos

            ones[c] = new_ones
            twos[c] = new_twos

    ans = 0
    b = ones[K]
    s = 0
    while b > 0:
        if b & 1:
            ans += s
        b >>= 1
        s += 1

    return ans
