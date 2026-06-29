


def solve():
    n, m = map(int, input().split())

    assert 1 <= n <= 100
    assert 1 <= m <= 100

    mat = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        if i % 2 == 0:
            print(*mat[i])
        else:
            print(*reversed(mat[i]))


if __name__ == "__main__":
    solve()
