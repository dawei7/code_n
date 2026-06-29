import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, k, s = data[idx:idx + 3]
        idx += 3
        if k == 1:
            if -n <= s <= n:
                if s >= 0:
                    ans = [1] * s + [0] * (n - s)
                else:
                    ans = [-1] * -s + [0] * (n + s)
                out.append(' '.join(map(str, ans)))
            else:
                out.append('-2')
            continue
        ans = []
        ok = True
        for _ in range(n):
            rem = s % k
            if rem == 0:
                digit = 0
            elif rem == 1:
                digit = 1
            elif rem == k - 1:
                digit = -1
            else:
                ok = False
                break
            ans.append(digit)
            s = (s - digit) // k
        if ok and s == 0:
            out.append(' '.join(map(str, ans)))
        else:
            out.append('-2')
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
