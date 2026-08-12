import math


def solve() -> int:
    """Find product d_1 * d_10 * d_100 * d_1000 * d_10000 * d_100000 * d_1000000.
    
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    parts = []
    length = 0
    i = 1
    while length < 1000000:
        s = str(i)
        parts.append(s)
        length += len(s)
        i += 1

    fraction = "".join(parts)
    indices = [1, 10, 100, 1000, 10000, 100000, 1000000]
    return math.prod(int(fraction[idx - 1]) for idx in indices)
