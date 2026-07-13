def solve(board: list[list[str]]) -> list[list[str]]:
    full = (1 << 9) - 1
    rows = [0] * 9
    columns = [0] * 9
    boxes = [0] * 9
    empty: list[tuple[int, int]] = []

    for row in range(9):
        for column in range(9):
            value = board[row][column]
            if value == ".":
                empty.append((row, column))
                continue
            bit = 1 << (int(value) - 1)
            box = (row // 3) * 3 + column // 3
            rows[row] |= bit
            columns[column] |= bit
            boxes[box] |= bit

    def fill(position: int) -> bool:
        if position == len(empty):
            return True

        best = position
        best_candidates = full
        for index in range(position, len(empty)):
            row, column = empty[index]
            box = (row // 3) * 3 + column // 3
            candidates = full & ~(rows[row] | columns[column] | boxes[box])
            if candidates.bit_count() < best_candidates.bit_count():
                best = index
                best_candidates = candidates
                if candidates.bit_count() <= 1:
                    break
        if best_candidates == 0:
            return False

        empty[position], empty[best] = empty[best], empty[position]
        row, column = empty[position]
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
        empty[position], empty[best] = empty[best], empty[position]
        return False

    fill(0)
    return board
