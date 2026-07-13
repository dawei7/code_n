def solve(grid: list[list[str]]) -> int:
    rows, columns = len(grid), len(grid[0])
    visited: set[tuple[int, int]] = set()
    islands = 0
    for row in range(rows):
        for column in range(columns):
            if grid[row][column] != "1" or (row, column) in visited:
                continue
            islands += 1
            visited.add((row, column))
            stack = [(row, column)]
            while stack:
                current_row, current_column = stack.pop()
                for next_row, next_column in ((current_row-1,current_column),(current_row+1,current_column),(current_row,current_column-1),(current_row,current_column+1)):
                    if 0 <= next_row < rows and 0 <= next_column < columns and grid[next_row][next_column] == "1" and (next_row, next_column) not in visited:
                        visited.add((next_row, next_column))
                        stack.append((next_row, next_column))
    return islands
