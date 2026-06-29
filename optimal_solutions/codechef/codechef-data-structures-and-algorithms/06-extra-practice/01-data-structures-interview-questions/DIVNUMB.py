import math
import sys

def lcm(x, y):
    return x * y // math.gcd(x, y)

def count_good(x, a, b, c, ab, bc, ac, abc):
    return x // a + x // b + x // c - x // ab - x // bc - x // ac + x // abc

def solve():
    input_data = sys.stdin.read().split()
    t = int(input_data[0])
    index = 1
    results = []
    for _ in range(t):
        N = int(input_data[index])
        a = int(input_data[index + 1])
        b = int(input_data[index + 2])
        c = int(input_data[index + 3])
        index += 4
        ab = lcm(a, b)
        bc = lcm(b, c)
        ac = lcm(a, c)
        abc = lcm(a, lcm(b, c))
        lo, hi = (1, 10 ** 18)
        while lo < hi:
            mid = (lo + hi) // 2
            if count_good(mid, a, b, c, ab, bc, ac, abc) < N:
                lo = mid + 1
            else:
                hi = mid
        results.append(str(lo))
    sys.stdout.write('\n'.join(results))


if __name__ == "__main__":
    solve()
