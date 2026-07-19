"""Optimal app-local solution for LeetCode 418."""


def solve(sentence: list[str], rows: int, cols: int) -> int:
    cycle = " ".join(sentence) + " "
    cycle_length = len(cycle)
    position = 0
    row = 0
    seen: dict[int, tuple[int, int]] = {}

    while row < rows:
        offset = position % cycle_length
        if offset in seen:
            previous_row, previous_position = seen[offset]
            cycle_rows = row - previous_row
            cycle_characters = position - previous_position
            repetitions = (rows - row) // cycle_rows
            if repetitions:
                row += repetitions * cycle_rows
                position += repetitions * cycle_characters
                continue
        else:
            seen[offset] = (row, position)

        position += cols
        if cycle[position % cycle_length] == " ":
            position += 1
        else:
            while position > 0 and cycle[(position - 1) % cycle_length] != " ":
                position -= 1
        row += 1

    return position // cycle_length
