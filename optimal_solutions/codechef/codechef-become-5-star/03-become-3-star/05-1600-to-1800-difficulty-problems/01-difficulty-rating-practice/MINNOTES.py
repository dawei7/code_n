import sys
from math import gcd

def solve():
    input = sys.stdin.read
    data = input().splitlines()
    index = 0
    t = int(data[index])
    index += 1
    tn = 0
    results = []
    for _ in range(t):
        n = int(data[index])
        tn += n
        index += 1
        a = [0] + list(map(int, data[index].split()))
        index += 1
        sum_ = [[0] * 2 for _ in range(n + 2)]
        dp = [[0] * 2 for _ in range(n + 2)]
        for i in range(1, n + 1):
            sum_[i][0] = sum_[i - 1][0] + a[i]
            sum_[n - i + 1][1] = sum_[n - i + 2][1] + a[n - i + 1]
            dp[i][0] = gcd(dp[i - 1][0], a[i])
            dp[n - i + 1][1] = gcd(dp[n - i + 2][1], a[n - i + 1])
        ans = float('inf')
        for i in range(1, n + 1):
            g = gcd(dp[i - 1][0], dp[i + 1][1])
            ans = min(ans, (0 if g == 0 else (sum_[i - 1][0] + sum_[i + 1][1]) // g) + 1)
        results.append(ans)
    print('\n'.join(map(str, results)))


if __name__ == "__main__":
    solve()
