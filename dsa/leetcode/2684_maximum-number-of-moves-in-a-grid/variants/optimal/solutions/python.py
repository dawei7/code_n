from typing import List

def solve(grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])

    # current_reachable_rows stores the row indices that are reachable in the current column.
    # Initially, all cells in the first column (column 0) are reachable.
    current_reachable_rows = set(range(m))
    max_moves = 0

    # Iterate through columns from 0 up to n-2.
    # A move takes us from column c to c+1.
    # If we make k moves, we reach column k.
    # The maximum possible moves is n-1 (reaching column n-1 from column 0).
    for c in range(n - 1):
        next_reachable_rows = set()
        
        # Iterate through all rows that were reachable in the current column 'c'.
        for r in current_reachable_rows:
            # Check the three possible moves: (r-1, c+1), (r, c+1), (r+1, c+1)
            for dr in [-1, 0, 1]:
                nr = r + dr  # next row
                nc = c + 1   # next column

                # Check boundary conditions for the next row
                if 0 <= nr < m:
                    # Check if the value in the next cell is strictly greater
                    if grid[nr][nc] > grid[r][c]:
                        next_reachable_rows.add(nr)
        
        # If no cells are reachable in the next column, we cannot make any more moves.
        if not next_reachable_rows:
            break
        
        # Update the set of reachable rows for the next iteration (next column).
        current_reachable_rows = next_reachable_rows
        # We successfully made one more move (moved to the next column).
        max_moves += 1
            
    return max_moves
