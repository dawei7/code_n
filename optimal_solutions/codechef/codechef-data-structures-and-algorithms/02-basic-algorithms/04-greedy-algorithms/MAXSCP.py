


def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = []
        flag = True

        for i in range(n):
            a.append(list(map(int, input().split())))

        for i in range(n):
            a[i].sort()

        sum1 = a[n - 1][n - 1]
        max1 = a[n - 1][n - 1]

        for i in range(n - 2, -1, -1):
            ok = False
            for j in range(n - 1, -1, -1):
                if a[i][j] < max1:
                    sum1 += a[i][j]
                    max1 = a[i][j]
                    ok = True
                    break
            if not ok:
                flag = False
                break

        if flag:
            print(sum1)
        else:
            print("-1")


if __name__ == "__main__":
    solve()
