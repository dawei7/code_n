# cook your dish here


def solve():
    MOD = 1000000007

    t = int(input())
    for _ in range(t):
        r, c, x = map(int, input().split())
        a = [list(map(int, input().split())) for _ in range(r)]
        b = [list(map(int, input().split())) for _ in range(r)]
        a1 = [[0] * x for _ in range(x)]

        for i in range(r):
            for j in range(c):
                a1[i % x][j % x] += a[i][j]
                a1[i % x][j % x] -= b[i][j]

        flag = 0
        for i in range(1, x):
            temp = a1[i][0] - a1[0][0]
            for j in range(1, x):
                if temp != a1[i][j] - a1[0][j]:
                    flag = 1

        if flag == 0:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    solve()
