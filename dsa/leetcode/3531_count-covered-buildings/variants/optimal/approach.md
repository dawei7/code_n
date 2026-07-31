## General

For a building at `[x, y]`, the existence of a building to its left depends only on the smallest occupied `y` coordinate in row `x`; a left building exists exactly when that minimum is smaller than `y`. The row maximum answers the symmetric right-side question. Likewise, the minimum and maximum `x` coordinates in column `y` answer whether buildings exist above and below.

Scan `buildings` once and maintain two hash maps. `row_bounds[x]` stores the minimum and maximum `y` in row `x`, while `column_bounds[y]` stores the minimum and maximum `x` in column `y`. A second scan counts `[x, y]` precisely when both strict inequalities hold in both maps.

The four inequalities are sufficient because each extreme is itself an occupied coordinate in the required row or column. They are also necessary: if a cardinal-direction building exists, the corresponding minimum or maximum is at least as far in that direction. Thus the test accepts exactly the covered buildings.

## Complexity detail

Let $B$ be the number of buildings. With expected constant-time hash-map operations, the two scans take $O(B)$ time. There are at most $B$ occupied rows and $B$ occupied columns, so the bound maps use $O(B)$ space. The numerical city size `n` does not require allocating an $n \times n$ grid.

## Alternatives and edge cases

- **Sort every row and column:** Sorting grouped coordinates also exposes the extremes but costs $O(B \log B)$ time in the worst case.
- **Compare every pair of buildings:** Directly searching all four directions for every coordinate takes $O(B^2)$ time.
- **Materialize the city grid:** An $n \times n$ array can require $O(n^2)$ space even though at most $10^5$ coordinates are occupied.
- **Strict directions:** A building cannot cover itself, so each comparison with a row or column extreme must be strict.
- **Diagonal coordinates:** Smaller or larger values on both axes do not count unless one coordinate is exactly shared.
- **Sparse long-distance cover:** Directional buildings need not be adjacent; only their relative coordinate and shared row or column matter.
- **Single occupied row or column:** Every building is missing at least one vertical or horizontal direction, so none is covered.
