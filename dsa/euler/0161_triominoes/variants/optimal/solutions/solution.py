def solve(rows: int = 12, cols: int = 9) -> int:
    """Find number of ways to tile a rows x cols grid with 6 triomino orientations.
    
    Time Complexity: O(rows * cols * 2^(2 * cols))
    Space Complexity: O(rows * cols * 2^(2 * cols))
    """
    if cols > rows:
        rows, cols = cols, rows

    shapes = [
        [(0, 0), (0, 1), (0, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 0), (1, 0), (0, 1)],
        [(0, 0), (1, 0), (1, 1)],
        [(0, 0), (0, 1), (1, 1)],
        [(0, 0), (1, 0), (1, -1)]
    ]

    memo = {}

    def dp(mask: int, cell: int) -> int:
        if cell == rows * cols:
            return 1 if mask == 0 else 0

        # If current cell is already covered, advance to next cell
        if mask & 1:
            return dp(mask >> 1, cell + 1)

        state = (cell, mask)
        if state in memo:
            return memo[state]

        r, c = divmod(cell, cols)
        ans = 0

        for shape in shapes:
            valid = True
            bit_offsets = []
            for dr, dc in shape:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    offset = dr * cols + (nc - c)
                    if (mask & (1 << offset)) != 0:
                        valid = False
                        break
                    bit_offsets.append(offset)
                else:
                    valid = False
                    break

            if valid:
                new_mask = mask
                for offset in bit_offsets:
                    new_mask |= (1 << offset)
                ans += dp(new_mask >> 1, cell + 1)

        memo[state] = ans
        return ans

    return dp(0, 0)
