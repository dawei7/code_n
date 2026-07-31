## General

A path's exact sum can grow, but only its remainder modulo `k` affects whether the completed path is counted. For each cell, retain a length-`k` vector where entry `r` counts paths reaching that cell with remainder $r$.

At cell `(row, column)`, every arriving path comes from the cell above or the cell to the left. For each prior remainder $r$, adding the current value moves its count to remainder `(r + grid[row][column]) % k`. Add both predecessor counts and reduce them modulo $10^9+7$. The top-left cell is initialized with one path in the remainder class of its own value.

Only one row of vectors is needed. Before a cell is replaced, `ways[column]` still represents the cell above; after the preceding column is processed, `ways[column - 1]` represents the cell to the left. Thus the rolling update preserves exactly the full two-dimensional recurrence. The destination's remainder-zero entry is the requested count.

## Complexity detail

Each of the $mn$ cells processes all $k$ remainder classes, so time is $O(mnk)$. The rolling array stores $n$ vectors of length $k$, giving $O(nk)$ auxiliary space. The modulus is applied during every transition.

## Alternatives and edge cases

- **Full three-dimensional table:** Storing every cell and remainder is direct but uses $O(mnk)$ space.
- **Enumerate individual paths:** Depth-first traversal is correct but exponential in the grid dimensions.
- **Single cell:** There is one path, counted only when that cell value is divisible by `k`.
- **Single row or column:** Exactly one path exists.
- **`k = 1`:** Every remainder is zero, so all monotone paths qualify.
- **Zero-valued cells:** They leave the current remainder unchanged.
- **Modulo reduction:** Counts, not cell sums, are reduced modulo $10^9+7$; remainder states use modulo `k`.
