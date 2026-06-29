import sys
MOD = 1000000007

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    max_n = 0
    ptr = 1
    for _ in range(t):
        max_n = max(max_n, data[ptr])
        ptr += 2 + data[ptr]
    fact = [1] * (max_n + 1)
    for i in range(1, max_n + 1):
        fact[i] = fact[i - 1] * i % MOD
    idx = 1
    out = []
    for _ in range(t):
        n, k = data[idx:idx + 2]
        idx += 2
        arr = data[idx:idx + n]
        idx += n
        odd_values = sum((x & 1 for x in arr))
        even_values = n - odd_values
        odd_positions = (n + 1) // 2
        even_positions = n // 2
        if k == 0:
            ans = fact[n] if odd_values in (0, n) else 0
        else:
            ans = 0
            if odd_values == odd_positions and even_values == even_positions:
                ans += fact[odd_positions] * fact[even_positions]
            if odd_values == even_positions and even_values == odd_positions:
                ans += fact[odd_positions] * fact[even_positions]
            ans %= MOD
        out.append(str(ans))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
