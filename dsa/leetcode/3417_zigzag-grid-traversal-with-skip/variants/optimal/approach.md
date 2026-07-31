## General

Process the rows from top to bottom. For an even row index, its columns appear from left to right; for an odd row index, they appear from right to left. These two ranges generate the complete zigzag sequence without copying or reversing any row.

Maintain one Boolean `take` flag for the entire traversal. It starts true at `(0, 0)` and flips after every encountered cell. Append a value exactly when the flag is true. Crucially, the flag is not reset when moving to another row, so even- and odd-width grids both preserve the global alternate-cell rule.

Every grid cell is generated once in the required zigzag position, and the flag equals true exactly at even zero-based positions in that generated order. Therefore the appended values are precisely the required visited cells, in order.

## Complexity detail

Let the grid contain $m$ rows and $n$ columns. Visiting every cell once takes $O(mn)$ time. The returned list contains $\lceil mn/2\rceil$ values and therefore uses $O(mn)$ output space; excluding the required output, the traversal uses $O(1)$ auxiliary space.

The benchmark defines `size` as the number of cells $mn$ and uses legal $5\times5$, $10\times10$, and $20\times20$ square grids, spanning 16x. The accepted direct traversal is linear in `size`. A correct baseline that rescans a materialized zigzag sequence from its beginning for every selected position takes $O((mn)^2)$ time and must fail only the scaling verdict.

## Alternatives and edge cases

- **Restart skipping on each row:** This is wrong for odd-width rows because the global visit/skip phase changes at the boundary.
- **Reverse copied rows:** It produces the right order but allocates unnecessary row copies; descending column indices avoid them.
- **Rescan a flattened sequence for every output position:** The output is correct, but repeated prefix scans make the method quadratic.
- **Even row width:** Each new row begins with the same visit/skip phase that the previous row began with, though its direction reverses.
- **Odd row width:** The next row begins with the opposite phase, which the persistent flag handles automatically.
- **Values and duplicates:** Traversal depends only on cell positions, so repeated values require no special handling.
- **Output lower bound:** Returning half of all cells already requires $\Theta(mn)$ output entries.
