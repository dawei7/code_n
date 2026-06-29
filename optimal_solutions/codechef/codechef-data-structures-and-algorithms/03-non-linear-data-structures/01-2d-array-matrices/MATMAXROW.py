


def solve():
    def firstOne(row, low, high):
        while low <= high:
            mid = low + (high - low) // 2
            if (mid == 0 or row[mid - 1] == 0) and row[mid] == 1:
                return mid
            elif row[mid] == 0:
                return firstOne(row, mid + 1, high)
            else:
                return firstOne(row, low, mid - 1)
        return -1

    def maxOneRow(mat):
        maxones = 0
        row_idx = 0
        for i, row in enumerate(mat):
            ones = len(row) - firstOne(row, 0, len(row) - 1)
            if ones > maxones:
                maxones = ones
                row_idx = i
        return row_idx + 1

    n, m = map(int, input().split())
    assert 1 <= n <= 100
    assert 1 <= m <= 100

    mat = [list(map(int, input().split())) for _ in range(n)]
    for row in mat:
        for elem in row:
            assert elem == 0 or elem == 1

    print(maxOneRow(mat))


if __name__ == "__main__":
    solve()
