


def solve():
    def is_valid_sudoku(board):
        # Check rows
        for row in board:
            seen = set()
            for num in row:
                if num != 0:
                    if num in seen:
                        return False
                    seen.add(num)

        # Check columns
        for col in range(9):
            seen = set()
            for row in range(9):
                num = board[row][col]
                if num != 0:
                    if num in seen:
                        return False
                    seen.add(num)

        # Check 3x3 sub-boxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        num = board[box_row + i][box_col + j]
                        if num != 0:
                            if num in seen:
                                return False
                            seen.add(num)
        return True

    import sys
    input_data = sys.stdin.read().strip().split()
    if input_data:
        t = int(input_data[0])
        index = 1
        results = []
        for _ in range(t):
            board = []
            for _ in range(9):
                row = list(map(int, input_data[index:index+9]))
                index += 9
                board.append(row)
            results.append("1" if is_valid_sudoku(board) else "0")
        sys.stdout.write("\n".join(results))


if __name__ == "__main__":
    solve()
