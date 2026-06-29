


def solve():
    def setZeroes(mat):
        n = len(mat)
        m = len(mat[0])
        first_col_zero = False

        # First pass: mark rows and columns
        for i in range(n):
            if mat[i][0] == 0:
                first_col_zero = True
            for j in range(1, m):
                if mat[i][j] == 0:
                    mat[i][0] = 0  # mark row
                    mat[0][j] = 0  # mark column

        # Second pass: set zeros using markers (bottom-up)
        for i in reversed(range(n)):
            for j in reversed(range(1, m)):
                if mat[i][0] == 0 or mat[0][j] == 0:
                    mat[i][j] = 0
            if first_col_zero:
                mat[i][0] = 0


if __name__ == "__main__":
    solve()
