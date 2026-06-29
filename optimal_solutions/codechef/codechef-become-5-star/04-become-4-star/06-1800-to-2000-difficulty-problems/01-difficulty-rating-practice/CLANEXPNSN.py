from collections import defaultdict


def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        D = defaultdict(list)
        for i in range(n):
            D[arr[i]] += [i]
        ans = [float('inf'),float('inf')]
        for i in range(1,n+1):
            L = D[i]
            if L:
                time = D[i][0]
                for j in range(1,len(L)):
                    bet = L[j] - L[j-1] - 1
                    if bet:
                        time = max(bet // 2 + bet % 2, time)
                time = max(n - D[i][-1] - 1, time)
                if time<ans[0]:
                    ans = [time,i]
        print(ans[1],ans[0])


if __name__ == "__main__":
    solve()
