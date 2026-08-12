import math


def solve(limit: int = 2000000000) -> int:
    """Find number of n <= limit representable as a^2 + k*b^2 for k in (1, 2, 3, 7).
    
    Time Complexity: O(limit / sqrt(k)) using sequential 250MB bitset sieving
    Space Complexity: O(limit / 8) bytes (~238 MB)
    """
    N = limit
    sz = (N >> 3) + 1

    bits = bytearray(sz)
    for b in range(1, int(math.sqrt(N)) + 1):
        b2 = b * b
        if b2 >= N:
            break
        max_a = int(math.sqrt(N - b2))
        for a in range(1, max_a + 1):
            val = a * a + b2
            bits[val >> 3] |= 1 << (val & 7)

    for k in (2, 3, 7):
        bits_k = bytearray(sz)
        for b in range(1, int(math.sqrt(N / k)) + 1):
            b2 = k * b * b
            if b2 >= N:
                break
            max_a = int(math.sqrt(N - b2))
            for a in range(1, max_a + 1):
                val = a * a + b2
                bits_k[val >> 3] |= 1 << (val & 7)

        for i in range(sz):
            bits[i] &= bits_k[i]

    return sum(bin(byte).count('1') for byte in bits)
