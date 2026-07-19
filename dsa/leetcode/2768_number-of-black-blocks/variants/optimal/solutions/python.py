def solve(m: int, n: int, coordinates: list[list[int]]) -> list[int]:
    # A 2x2 subgrid is identified by its top-left corner (r, c).
    # Valid top-left corners are 0 <= r < m-1 and 0 <= c < n-1.
    # A black cell at (r, c) affects subgrids with top-left corners:
    # (r-1, c-1), (r-1, c), (r, c-1), (r, c)
    
    counts = {}
    for r, c in coordinates:
        for dr in range(-1, 1):
            for dc in range(-1, 1):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m - 1 and 0 <= nc < n - 1:
                    counts[(nr, nc)] = counts.get((nr, nc), 0) + 1
    
    result = [0] * 5
    # Count how many subgrids have 1, 2, 3, or 4 black cells
    for val in counts.values():
        result[val] += 1
    
    # Total possible 2x2 subgrids
    total_subgrids = (m - 1) * (n - 1)
    # Subgrids with 0 black cells = Total - subgrids with at least 1 black cell
    result[0] = total_subgrids - sum(result[1:])
    
    return result
