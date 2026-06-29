import sys
MOD = 1000000007

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    max_n = 0
    cases = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        values = sorted(data[idx:idx + n])
        idx += n
        max_n = max(max_n, n)
        cases.append(values)
    pow2 = [1] * (max_n + 1)
    for i in range(1, max_n + 1):
        pow2[i] = pow2[i - 1] * 2 % MOD
    out = []
    for values in cases:
        n = len(values)
        answer = 0
        for i, value in enumerate(values):
            answer = (answer + value * (pow2[i] - pow2[n - 1 - i])) % MOD
        out.append(str(answer))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
