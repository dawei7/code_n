from array import array


def solve(grid: list[list[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    total = rows * cols
    directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
    values = [value for row in grid for value in row]

    def ordered_indices(dr: int, dc: int):
        row_range = range(rows - 1, -1, -1) if dr > 0 else range(rows)
        col_range = range(cols - 1, -1, -1) if dc > 0 else range(cols)
        for row in row_range:
            base = row * cols
            for col in col_range:
                yield row, col, base + col

    straight: list[tuple[array, array]] = []
    for dr, dc in directions:
        take_two = array("H", [0]) * total
        take_zero = array("H", [0]) * total
        for row, col, idx in ordered_indices(dr, dc):
            next_row, next_col = row + dr, col + dc
            next_idx = next_row * cols + next_col
            has_next = 0 <= next_row < rows and 0 <= next_col < cols
            if values[idx] == 2:
                take_two[idx] = 1 + (take_zero[next_idx] if has_next else 0)
            elif values[idx] == 0:
                take_zero[idx] = 1 + (take_two[next_idx] if has_next else 0)
        straight.append((take_two, take_zero))

    answer = 1 if any(value == 1 for value in values) else 0
    for direction, (dr, dc) in enumerate(directions):
        turn_direction = (direction + 1) % 4
        turn_dr, turn_dc = directions[turn_direction]
        turn_two, turn_zero = straight[turn_direction]
        best_two = array("H", [0]) * total
        best_zero = array("H", [0]) * total
        for row, col, idx in ordered_indices(dr, dc):
            next_row, next_col = row + dr, col + dc
            next_idx = next_row * cols + next_col
            has_next = 0 <= next_row < rows and 0 <= next_col < cols
            turn_row, turn_col = row + turn_dr, col + turn_dc
            turn_idx = turn_row * cols + turn_col
            has_turn = 0 <= turn_row < rows and 0 <= turn_col < cols
            if values[idx] == 2:
                keep = best_zero[next_idx] if has_next else 0
                turn = turn_zero[turn_idx] if has_turn else 0
                best_two[idx] = 1 + max(keep, turn)
            elif values[idx] == 0:
                keep = best_two[next_idx] if has_next else 0
                turn = turn_two[turn_idx] if has_turn else 0
                best_zero[idx] = 1 + max(keep, turn)
        for row in range(rows):
            next_row = row + dr
            if next_row < 0 or next_row >= rows:
                continue
            row_base = row * cols
            next_base = next_row * cols
            for col in range(cols):
                next_col = col + dc
                if values[row_base + col] == 1 and 0 <= next_col < cols:
                    answer = max(answer, 1 + best_two[next_base + next_col])
    return answer
