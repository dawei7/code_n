from collections import deque


def solve(classroom: list[str], energy: int) -> int:
    rows = len(classroom)
    columns = len(classroom[0])
    litter_bits: dict[tuple[int, int], int] = {}
    litter_count = 0
    start = (0, 0)

    for row in range(rows):
        for column in range(columns):
            cell = classroom[row][column]
            if cell == "S":
                start = (row, column)
            elif cell == "L":
                litter_bits[(row, column)] = 1 << litter_count
                litter_count += 1

    full_mask = (1 << litter_count) - 1
    queue = deque([(start[0], start[1], 0, energy, 0)])
    best_energy = {(start[0], start[1], 0): energy}

    while queue:
        row, column, mask, remaining, moves = queue.popleft()
        if mask == full_mask:
            return moves
        if remaining < best_energy[(row, column, mask)]:
            continue
        if remaining == 0:
            continue

        for next_row, next_column in (
            (row - 1, column),
            (row + 1, column),
            (row, column - 1),
            (row, column + 1),
        ):
            if not (0 <= next_row < rows and 0 <= next_column < columns):
                continue
            cell = classroom[next_row][next_column]
            if cell == "X":
                continue

            next_mask = mask | litter_bits.get((next_row, next_column), 0)
            next_energy = energy if cell == "R" else remaining - 1
            key = (next_row, next_column, next_mask)
            if next_energy > best_energy.get(key, -1):
                best_energy[key] = next_energy
                queue.append((next_row, next_column, next_mask, next_energy, moves + 1))

    return -1
