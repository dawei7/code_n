import sys
MOD = 1000000007

def precompute(limit: int):
    chef = [0] * limit
    other = [0] * limit
    chef[0] = 1
    ans = [0] * (limit + 1)
    for total in range(limit):
        for move in (1, 2, 3, 4):
            nxt = total + move
            if nxt >= limit:
                continue
            if move == 1:
                other[nxt] = (other[nxt] + chef[total]) % MOD
                chef[nxt] = (chef[nxt] + other[total]) % MOD
            else:
                chef[nxt] = (chef[nxt] + chef[total]) % MOD
                other[nxt] = (other[nxt] + other[total]) % MOD
    prefix = [0] * (limit + 1)
    for i, value in enumerate(chef):
        prefix[i + 1] = (prefix[i] + value) % MOD
    for l in range(1, limit + 1):
        left = max(0, l - 4)
        ans[l] = (prefix[l] - prefix[left]) % MOD
    return ans

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    values = data[1:1 + t]
    ans = precompute(max(values) if values else 1)
    sys.stdout.write('\n'.join((str(ans[x]) for x in values)))


if __name__ == "__main__":
    solve()
