


def solve():
    def areaOfIsland(mat, i, j):
        if 0 <= i < len(mat) and 0 <= j < len(mat[0]) and mat[i][j] == 1:
            mat[i][j] = 0
            return 1 + areaOfIsland(mat, i + 1, j) + areaOfIsland(mat, i - 1, j) \
                   + areaOfIsland(mat, i, j - 1) + areaOfIsland(mat, i, j + 1)
        return 0

    def maxAreaOfIsland(mat):
        max_area = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    max_area = max(max_area, areaOfIsland(mat, i, j))
        return max_area

    if __name__ == "__main__":
        n, m = map(int, input().split())

        assert 1 <= n <= 100
        assert 1 <= m <= 100

        mat = [list(map(int, input().split())) for _ in range(n)]

        print(maxAreaOfIsland(mat))


if __name__ == "__main__":
    solve()
