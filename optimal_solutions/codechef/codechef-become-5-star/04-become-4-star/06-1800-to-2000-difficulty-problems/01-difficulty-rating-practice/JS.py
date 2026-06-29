import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    inf = 10 ** 9
    for _ in range(t):
        n = data[idx]
        idx += 1
        parities = [value & 1 for value in data[idx:idx + n]]
        idx += n
        next_pos = [[n] * 2 for _ in range(n)]
        last = [n, n]
        for i in range(n - 1, -1, -1):
            next_pos[i][0] = last[0]
            next_pos[i][1] = last[1]
            last[parities[i]] = i
        dp = [[inf, inf] for _ in range(n)]
        dp[0][0] = 0
        for i in range(n):
            for used in range(2):
                if dp[i][used] >= inf:
                    continue
                same = next_pos[i][parities[i]]
                if same < n:
                    dp[same][used] = min(dp[same][used], dp[i][used] + 1)
                diff = next_pos[i][1 - parities[i]]
                if diff < n and used == 0:
                    dp[diff][1] = min(dp[diff][1], dp[i][used] + 1)
        out.append(str(min(dp[-1])))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
