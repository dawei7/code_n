


def solve():
    def countNegatives(matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        row_index = 0
        col_index = cols - 1
        negatives_count = 0

        while row_index < rows:
            while col_index >= 0 and matrix[row_index][col_index] < 0:
                col_index -= 1
            negatives_count += cols - col_index - 1
            row_index += 1

        return negatives_count

    n, m = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]
    print(countNegatives(mat))


if __name__ == "__main__":
    solve()
