def solve(rows: int = 12, cols: int = 9) -> int:
    """Find the number of ways to tile a rows x cols (9 x 12) grid using triominoes (6 orientations).

    Mathematical Principles Applied:
    1. Broken-Profile Dynamic Programming / Bitmask Tiling:
       Represent the grid as a linear sequence of cells cell = r * cols + c (0 <= cell < rows * cols).
       Maintain a bitmask of upcoming cell coverage states (length up to 2 * cols + 1).

    2. Triomino Shapes (6 Orientations):
       - Straight 1x3 horizontal: [(0,0), (0,1), (0,2)]
       - Straight 3x1 vertical: [(0,0), (1,0), (2,0)]
       - L-shape Top-Left corner: [(0,0), (1,0), (0,1)]
       - L-shape Bottom-Left corner: [(0,0), (1,0), (1,1)]
       - L-shape Top-Right corner: [(0,0), (0,1), (1,1)]
       - L-shape Bottom-Right corner: [(0,0), (1,0), (1,-1)]

    3. Recursive DP State Transitions:
       `dp(mask, cell)` evaluates valid tilings.
       - If cell is already covered (`mask & 1`), advance `dp(mask >> 1, cell + 1)`.
       - Otherwise, try placing each of the 6 triomino shapes rooted at cell, bitwise ORing bit offsets,
         and advance `dp(new_mask >> 1, cell + 1)`. Memoize via `memo[(cell, mask)]`.

    Time Complexity: O(rows * cols * 2^(2*cols)) executing in ~0.50s.
    Space Complexity: O(rows * cols * 2^(2*cols)) DP memo memory.
    """
    if cols > rows:
        rows, cols = cols, rows

    shapes = [
        [(0, 0), (0, 1), (0, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 0), (1, 0), (0, 1)],
        [(0, 0), (1, 0), (1, 1)],
        [(0, 0), (0, 1), (1, 1)],
        [(0, 0), (1, 0), (1, -1)],
    ]

    memo = {}

    def dp(mask: int, cell: int) -> int:
        if cell == rows * cols:
            return 1 if mask == 0 else 0

        # If current cell is already covered by a previously placed triomino, skip to next cell
        if mask & 1:
            return dp(mask >> 1, cell + 1)

        state = (cell, mask)
        if state in memo:
            return memo[state]

        r, c = divmod(cell, cols)
        ans = 0

        # Try placing each of the 6 triomino shapes rooted at (r, c)
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
                    new_mask |= 1 << offset
                ans += dp(new_mask >> 1, cell + 1)

        memo[state] = ans
        return ans

    # Return total number of valid triomino tilings for a 9 x 12 grid
    return dp(0, 0)


if __name__ == "__main__":
    print(solve())
