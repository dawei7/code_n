import sys
from functools import lru_cache
from itertools import combinations

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        f = data[idx:idx + n + 1]
        idx += n + 1
        bit_counts = []
        limit = n.bit_length()
        for bit in range(limit):
            p = 1 << bit
            delta = (f[p] - f[0]) // p
            bit_counts.append((3 - delta) // 2)

        @lru_cache(None)
        def build(bit: int, a: int, b: int, c: int):
            if bit < 0:
                return (a, b, c) if a <= n and b <= n and (c <= n) else None
            p = 1 << bit
            ones = bit_counts[bit]
            for chosen in combinations(range(3), ones):
                vals = [a, b, c]
                for pos in chosen:
                    vals[pos] |= p
                if vals[0] <= n and vals[1] <= n and (vals[2] <= n):
                    res = build(bit - 1, vals[0], vals[1], vals[2])
                    if res is not None:
                        return res
            return None
        nums = build(limit - 1, 0, 0, 0)
        out.append(f'{nums[0]} {nums[1]} {nums[2]}')
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
