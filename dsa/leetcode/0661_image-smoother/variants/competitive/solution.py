class Solution:
    def imageSmoother(self, img):
        rows = len(img)
        columns = len(img[0])
        result = [[0] * columns for _ in range(rows)]
        for row in range(rows):
            for column in range(columns):
                total = count = 0
                for next_row in range(max(0, row - 1), min(rows, row + 2)):
                    for next_column in range(max(0, column - 1), min(columns, column + 2)):
                        total += img[next_row][next_column]
                        count += 1
                result[row][column] = total // count
        return result
