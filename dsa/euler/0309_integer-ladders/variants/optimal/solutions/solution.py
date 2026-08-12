import math


def solve(limit: int = 1000000) -> int:
    """Find the number of triplets (x, y, h) with x < y < limit producing integer street width w.
    
    Time Complexity: O(limit * log(limit)) via Pythagorean Right Triangle Pairing
    Space Complexity: O(limit)
    """
    if limit < 5:
        return 0

    legs = [[] for _ in range(limit)]

    max_u = int(limit**0.5) + 1
    for u in range(2, max_u):
        for v in range(1 + (u % 2), u, 2):
            if math.gcd(u, v) == 1:
                hyp = u * u + v * v
                if hyp >= limit:
                    break
                l1 = u * u - v * v
                l2 = 2 * u * v

                k = 1
                while k * hyp < limit:
                    w1, a1 = k * l1, k * l2
                    w2, a2 = k * l2, k * l1
                    legs[w1].append(a1)
                    legs[w2].append(a2)
                    k += 1

    ans = 0
    for w in range(1, limit):
        a_list = legs[w]
        n_a = len(a_list)
        if n_a < 2:
            continue
        for i in range(n_a):
            a = a_list[i]
            for j in range(i + 1, n_a):
                b = a_list[j]
                if (a * b) % (a + b) == 0:
                    ans += 1

    return ans

