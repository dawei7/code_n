import bisect
import sys
MOD = 1000000007

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        p, q, r = data[idx:idx + 3]
        idx += 3
        a = sorted(data[idx:idx + p])
        idx += p
        b = data[idx:idx + q]
        idx += q
        c = sorted(data[idx:idx + r])
        idx += r
        pref_a = [0]
        for value in a:
            pref_a.append((pref_a[-1] + value) % MOD)
        pref_c = [0]
        for value in c:
            pref_c.append((pref_c[-1] + value) % MOD)
        answer = 0
        for y in b:
            ca = bisect.bisect_right(a, y)
            cc = bisect.bisect_right(c, y)
            left = (pref_a[ca] + ca * y) % MOD
            right = (pref_c[cc] + cc * y) % MOD
            answer = (answer + left * right) % MOD
        out.append(str(answer))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
