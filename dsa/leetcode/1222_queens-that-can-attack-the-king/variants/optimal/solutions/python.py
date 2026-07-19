def solve(queens: list[list[int]], king: list[int]) -> list[list[int]]:
    occupied = {tuple(queen) for queen in queens}
    answer = []
    for row_change, column_change in ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)):
        row, column = king[0] + row_change, king[1] + column_change
        while 0 <= row < 8 and 0 <= column < 8:
            if (row, column) in occupied:
                answer.append([row, column])
                break
            row += row_change
            column += column_change
    return answer
