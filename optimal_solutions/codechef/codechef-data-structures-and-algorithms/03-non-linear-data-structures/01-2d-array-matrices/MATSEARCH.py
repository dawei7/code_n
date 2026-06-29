


def solve():
    def search_in_matrix(matrix, target):
        numRows = len(matrix)
        numCols = len(matrix[0])

        start, end = 0, numRows * numCols - 1

        while start <= end:
            mid = start + (end - start) // 2
            midElement = matrix[mid // numCols][mid % numCols]

            if target == midElement:
                return True
            elif target < midElement:
                end = mid - 1
            else:
                start = mid + 1

        return False

    n, m, x = map(int, input().split())

    if n == 0 or m == 0:
        print("NO")
        exit()

    mat = [list(map(int, input().split())) for _ in range(n)]

    if search_in_matrix(mat, x):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    solve()
