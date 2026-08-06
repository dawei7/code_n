def solve(board: list[list[str]]) -> None:
    full = (1 << 9) - 1
    rows = [0] * 9
    columns = [0] * 9
    boxes = [0] * 9
    empty_cells: list[tuple[int, int]] = []

    for row in range(9):
        for column in range(9):
            value = board[row][column]
            if value == ".":
                empty_cells.append((row, column))
                continue
            bit = 1 << (int(value) - 1)
            box = (row // 3) * 3 + column // 3
            rows[row] |= bit
            columns[column] |= bit
            boxes[box] |= bit

    def fill(position: int) -> bool:
        if position == len(empty_cells):
            return True

        best_position = position
        best_candidates = full
        for i in range(position, len(empty_cells)):
            row, column = empty_cells[i]
            box = (row // 3) * 3 + column // 3
            candidates = full & ~(rows[row] | columns[column] | boxes[box])
            if candidates.bit_count() < best_candidates.bit_count():
                best_position = i
                best_candidates = candidates
                if candidates.bit_count() <= 1:
                    break
        if best_candidates == 0:
            return False

        empty_cells[position], empty_cells[best_position] = empty_cells[best_position], empty_cells[position]
        row, column = empty_cells[position]
        box = (row // 3) * 3 + column // 3
        candidates = full & ~(rows[row] | columns[column] | boxes[box])
        while candidates:
            bit = candidates & -candidates
            candidates ^= bit
            board[row][column] = str(bit.bit_length())
            rows[row] |= bit
            columns[column] |= bit
            boxes[box] |= bit
            if fill(position + 1):
                return True
            rows[row] ^= bit
            columns[column] ^= bit
            boxes[box] ^= bit
            board[row][column] = "."
        empty_cells[position], empty_cells[best_position] = empty_cells[best_position], empty_cells[position]
        return False

    fill(0)
