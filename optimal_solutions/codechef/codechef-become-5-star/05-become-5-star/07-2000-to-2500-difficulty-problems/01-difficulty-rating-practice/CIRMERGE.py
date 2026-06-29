# cook your dish here


def solve():
    for _ in range(int(input())):
        n = int(input())
        tne = list(map(int,input().split()))
        if n==2: print(sum(tne))
        n = n*2
        tne = tne + tne
        dp = [[float('inf')]*(n+1) for _ in range(n+1)]
        sk = [[None]*(n+1) for _ in range(n+1)]
        for i in range(n+1): dp[i][i], sk[i][i] = 0, i
        sm = [tne[0]]
        for i in range(1, n): sm.append(sm[i-1]+tne[i])
        for gap in range(1, n//2):
            for i in range(n-gap):
                j = i + gap
                tmp = sm[j] - [0, sm[i-1]][i > 0]
                i1, j1 = sk[i][j-1], sk[i+1][j]+1
                for k in range(i1, j1):
                    if dp[i][j] > dp[i][k] + dp[k+1][j] + tmp:
                        dp[i][j], sk[i][j] = dp[i][k] + dp[k+1][j] + tmp, k
        print(min([dp[i][i+n//2-1] for i in range(n//2)]))


if __name__ == "__main__":
    solve()
