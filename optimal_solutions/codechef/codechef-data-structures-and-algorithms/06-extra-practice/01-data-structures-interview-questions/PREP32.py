import sys

def edit_distance(a, b):
    n, m = (len(a), len(b))
    if n == 0:
        return m
    if m == 0:
        return n
    dp = list(range(n + 1))
    for j in range(1, m + 1):
        prev_dp = dp[0]
        dp[0] = j
        for i in range(1, n + 1):
            temp = dp[i]
            cost = 0 if a[i - 1] == b[j - 1] else 1
            dp[i] = min(dp[i] + 1, dp[i - 1] + 1, prev_dp + cost)
            prev_dp = temp
    return dp[n]

def solve():
    data = sys.stdin.read().splitlines()
    t = int(data[0])
    index = 1
    outputs = []
    for _ in range(t):
        a = data[index].strip()
        b = data[index + 1].strip()
        index += 2
        outputs.append(str(edit_distance(a, b)))
    sys.stdout.write('\n'.join(outputs))


if __name__ == "__main__":
    solve()
