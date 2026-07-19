from itertools import combinations

def solve(matrix: list[list[int]], num_select: int) -> int:
    m = len(matrix)
    n = len(matrix[0])

    # Convert each row into a bitmask for efficient comparison
    row_masks = []
    for row in matrix:
        mask = 0
        for j in range(n):
            if row[j] == 1:
                mask |= (1 << j)
        row_masks.append(mask)

    max_covered = 0

    # Generate all combinations of column indices to select
    for cols in combinations(range(n), num_select):
        # Create a mask representing the selected columns
        selection_mask = 0
        for col in cols:
            selection_mask |= (1 << col)

        # Count rows covered by this selection
        # A row is covered if (row_mask & selection_mask) == row_mask
        # This is equivalent to (row_mask & ~selection_mask) == 0
        count = 0
        for r_mask in row_masks:
            if (r_mask & selection_mask) == r_mask:
                count += 1

        if count > max_covered:
            max_covered = count

    return max_covered
