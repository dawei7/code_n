


def solve():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        ans = [0]*n
        for i in range(0, n, m):
            mark = [0]*(m+1)
            for j in range(i, min(n, i+m)):
                if mark[a[j]] == 1: continue
                ans[j] = a[j]
                mark[a[j]] = 1
            for j in range(i, min(i+m, n)):
                if ans[j] > 0: continue
                while mark[len(mark)-1] == 1: mark.pop()
                ans[j] = len(mark) - 1
                mark.pop()
        print(*ans)


if __name__ == "__main__":
    solve()
