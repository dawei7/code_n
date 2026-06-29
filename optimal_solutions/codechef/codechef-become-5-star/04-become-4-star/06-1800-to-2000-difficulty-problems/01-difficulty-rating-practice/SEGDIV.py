# cook your dish here


def solve():
    dp = [1,2] + [0]*499
    for i in range(2, len(dp)):
        dp[i] = dp[i - 2] + 4
    for _ in range(int(input())):
        print(*dp[:int(input())])


if __name__ == "__main__":
    solve()
