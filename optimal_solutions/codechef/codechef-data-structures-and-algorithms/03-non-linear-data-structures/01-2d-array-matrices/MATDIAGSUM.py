


def solve():
    def diagonalSum(mat):
        n = len(mat)
        sum = 0
        for i in range(n):
            if i != n - i - 1:
                sum += mat[i][i] + mat[i][n - i - 1]
            else:
                sum += mat[i][i]
        return sum

    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(n)]
    print(diagonalSum(mat))


if __name__ == "__main__":
    solve()
