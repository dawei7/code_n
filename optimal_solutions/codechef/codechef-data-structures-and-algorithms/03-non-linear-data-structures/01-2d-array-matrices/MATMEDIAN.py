


def solve():
    def countElementsSmallerThanMid(row, midValue):
        lowIndex, highIndex = 0, len(row) - 1
        while lowIndex <= highIndex:
            middleIndex = (lowIndex + highIndex) // 2
            if row[middleIndex] <= midValue:
                lowIndex = middleIndex + 1
            else:
                highIndex = middleIndex - 1
        return lowIndex

    def findMedianValue(matrix):
        rowCount, columnCount = len(matrix), len(matrix[0])
        lowValue, highValue = float('inf'), float('-inf')

        for row in matrix:
            lowValue = min(lowValue, min(row))
            highValue = max(highValue, max(row))

        while lowValue <= highValue:
            midValue = (lowValue + highValue) // 2
            count = sum(countElementsSmallerThanMid(row, midValue) for row in matrix)
            if count <= (rowCount * columnCount) // 2:
                lowValue = midValue + 1
            else:
                highValue = midValue - 1
        return lowValue

    n, m = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]
    print(findMedianValue(mat))


if __name__ == "__main__":
    solve()
