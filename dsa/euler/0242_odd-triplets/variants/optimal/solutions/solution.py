def solve(limit: int = 10**12) -> int:
    """Find number of odd-triplets [n, k, f(n, k)] with n <= limit.
    
    Time Complexity: O(log(limit)) via digit DP bit-counting
    Space Complexity: O(1)
    """
    if limit < 1:
        return 0

    # Valid n must be of form 4m + 1.
    # f(4m+1, 2j+1) is odd iff j is a bitwise submask of m.
    # Number of valid k for a given m is 2^(popcount(m)).
    # We need sum_{m=0}^{M} 2^(popcount(m)) where M = (limit - 1) // 4.
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

