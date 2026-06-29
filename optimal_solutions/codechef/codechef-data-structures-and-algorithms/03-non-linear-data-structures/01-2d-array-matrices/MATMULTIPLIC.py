


def solve():
    m, n = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(m)]

    n, p = map(int, input().split())
    assert n == len(a[0])

    b = [list(map(int, input().split())) for _ in range(n)]

    mul = [[0 for _ in range(p)] for _ in range(m)]

    for i in range(m):
        for j in range(p):
            for k in range(n):
                mul[i][j] += a[i][k] * b[k][j]
            print(mul[i][j], end=" ")
        print()


if __name__ == "__main__":
    solve()
