import sys

MAX_FUEL = 1000


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    INF = 10**9
    for _ in range(t):
        n = data[idx]
        idx += 1
        houses = data[idx:idx + n]
        idx += n
        cans = data[idx:idx + n]
        idx += n
        dp = [INF] * (MAX_FUEL + 1)
        dp[0] = 0
        for can in cans:
            for amount in range(can, MAX_FUEL + 1):
                if dp[amount - can] + 1 < dp[amount]:
                    dp[amount] = dp[amount - can] + 1
        out.append(str(sum(dp[2 * h] for h in houses)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
