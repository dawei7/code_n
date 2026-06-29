


def solve():
    def diagonalSort(mat):
        row, col = len(mat), len(mat[0])
        d = {}
        for i in range(row):
            for j in range(col):
                if i - j not in d:
                    d[i - j] = []
                d[i - j].append(mat[i][j])

        for key in d:
            d[key].sort()

        for i in range(row):
            for j in range(col):
                mat[i][j] = d[i - j].pop(0)

        return mat

    n, m = map(int, input().split())
    assert 1 <= n <= 100
    assert 1 <= m <= 100

    mat = [list(map(int, input().split())) for _ in range(n)]
    mat = diagonalSort(mat)

    for row in mat:
        print(*row)


if __name__ == "__main__":
    solve()
