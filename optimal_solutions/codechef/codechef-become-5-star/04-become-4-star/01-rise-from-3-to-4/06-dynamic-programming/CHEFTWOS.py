import sys
MOD = 1000000007

def advance(state: int, ch: int) -> int:
    if state == 0:
        return 0 if ch == 1 else 1
    if state == 1:
        return 2 if ch == 2 else -1
    return 0 if ch == 1 else -1

def count_swaps(a: bytes, b: bytes) -> int:
    n = len(a)
    if n == 1:
        return 2
    dp = [[0, 0, 0] for _ in range(3)]
    dp[0][0] = 1
    for i in range(n - 1):
        ndp = [[0, 0, 0] for _ in range(3)]
        choices = ((a[i] - 48, b[i] - 48), (b[i] - 48, a[i] - 48))
        for s1 in range(3):
            for s2 in range(3):
                value = dp[s1][s2]
                if not value:
                    continue
                for c1, c2 in choices:
                    ns1 = advance(s1, c1)
                    ns2 = advance(s2, c2)
                    if ns1 != -1 and ns2 != -1:
                        ndp[ns1][ns2] = (ndp[ns1][ns2] + value) % MOD
        dp = ndp
    return dp[0][0] * 2 % MOD

def solve() -> None:
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return
    t = int(tokens[0])
    idx = 1
    out: list[str] = []
    for _ in range(t):
        a = tokens[idx]
        b = tokens[idx + 1]
        idx += 2
        out.append(str(count_swaps(a, b)))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
