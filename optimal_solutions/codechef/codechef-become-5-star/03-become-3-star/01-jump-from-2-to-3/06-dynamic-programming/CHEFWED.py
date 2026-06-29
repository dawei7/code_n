import sys

def minimum_inefficiency(families: list[int], table_cost: int) -> int:
    n = len(families)
    dp = [0] + [10 ** 12] * n
    for start in range(n):
        counts = [0] * 101
        conflict = 0
        base = dp[start] + table_cost
        for end in range(start, n):
            family = families[end]
            counts[family] += 1
            if counts[family] == 2:
                conflict += 2
            elif counts[family] > 2:
                conflict += 1
            value = base + conflict
            if value < dp[end + 1]:
                dp[end + 1] = value
    return dp[n]

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out: list[str] = []
    for _ in range(t):
        n = data[idx]
        table_cost = data[idx + 1]
        idx += 2
        families = data[idx:idx + n]
        idx += n
        out.append(str(minimum_inefficiency(families, table_cost)))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
