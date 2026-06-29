import sys
MOD = 1000000007

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, x = (data[idx], data[idx + 1])
        idx += 2
        out.append(str(x * pow(2, n - 1, MOD) % MOD))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
