import urllib.request


def solve_sudoku(grid: list[list[int]]) -> bool:
    """Solve 9x9 Sudoku grid using MRV (Minimum Remaining Values) backtracking."""
    empty_cell = None
    min_candidates = 10
    best_valid = None

    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                used = set(grid[r])
                used.update(grid[i][c] for i in range(9))
                box_r, box_c = (r // 3) * 3, (c // 3) * 3
                used.update(grid[box_r + i][box_c + j] for i in range(3) for j in range(3))
                valid = [v for v in range(1, 10) if v not in used]

                if len(valid) < min_candidates:
                    min_candidates = len(valid)
                    empty_cell = (r, c)
                    best_valid = valid
                    if min_candidates == 0:
                        return False  # Dead end

    if empty_cell is None:
        return True  # Grid fully solved

    r, c = empty_cell
    for val in best_valid:
        grid[r][c] = val
        if solve_sudoku(grid):
            return True
        grid[r][c] = 0

    return False


def solve() -> int:
    """Solve 50 Sudoku puzzles from sudoku.txt and return sum of top-left 3-digit numbers.
    
    Time Complexity: O(50 * SudokuSolve)
    Space Complexity: O(1)
    """
    url = "https://projecteuler.net/resources/documents/0096_sudoku.txt"
    with urllib.request.urlopen(url, timeout=5) as resp:
        text = resp.read().decode("utf-8")

    lines = [line.strip() for line in text.strip().splitlines() if line.strip()]

    total_sum = 0
    i = 0
    while i < len(lines):
        if lines[i].startswith("Grid"):
            i += 1
            grid = []
            for _ in range(9):
                grid.append([int(c) for c in lines[i]])
                i += 1

            solve_sudoku(grid)
            top_left_3 = grid[0][0] * 100 + grid[0][1] * 10 + grid[0][2]
            total_sum += top_left_3

    return total_sum
