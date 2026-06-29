import sys
MOD = 1000000007

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    cases = []
    idx = 1
    max_n = 0
    max_k = 0
    for _ in range(t):
        n, m, k = (data[idx], data[idx + 1], data[idx + 2])
        idx += 3
        cases.append((n, m, k))
        max_n = max(max_n, n)
        max_k = max(max_k, min(n, k))
    stirling = [[0] * (max_k + 1) for _ in range(max_n + 1)]
    stirling[0][0] = 1
    for n in range(1, max_n + 1):
        upper = min(n, max_k)
        for k in range(1, upper + 1):
            stirling[n][k] = (stirling[n - 1][k - 1] + k * stirling[n - 1][k]) % MOD
    out: list[str] = []
    for n, m, k in cases:
        limit = min(n, m, k)
        falling = 1
        answer = 0
        for used in range(1, limit + 1):
            falling = falling * (m - used + 1) % MOD
            answer = (answer + falling * stirling[n][used]) % MOD
        out.append(str(answer))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
