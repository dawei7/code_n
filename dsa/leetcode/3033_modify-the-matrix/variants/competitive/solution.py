class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        answer = [row[:] for row in matrix]

        for col in range(len(matrix[0])):
            column_maximum = max(row[col] for row in matrix)
            for row in range(len(matrix)):
                if answer[row][col] == -1:
                    answer[row][col] = column_maximum

        return answer
