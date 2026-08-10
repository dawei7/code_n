## General

The required path count is at most four, so the source does not attempt a general obstacle search. It selects one small top-left “core” with exactly `k` paths to the core's bottom-right cell, then connects that cell to the grid's real destination through a corridor with exactly one continuation.

The number of complete paths is therefore:

$$
\text{paths through core}\times
\text{continuations through tail}
=k\cdot1=k.
$$

Every other cell begins blocked, which prevents accidental routes outside this intended structure.

**Starting from obstacles**

The source creates an `m\times n` mutable grid filled with `"#"`. It later opens only core and corridor cells.

This direction is safer for a construction proof than starting free and trying to block alternatives: any route must remain inside the explicitly opened shape.

**Core for `k=1`**

The core dimensions are `1\times1`. Its only cell is the start and core exit, so there is one zero-move path to that exit.

The later corridor carries that one path to the actual destination. This works for every positive `m,n`, including a one-row or one-column grid.

**Core for `k=2`**

When `m\ge2` and `n\ge2`, the source opens a full `2\times2` core.

From its top-left to bottom-right, a route needs one right and one down move. Their two possible orders are:

$$
RD,\quad DR.
$$

Thus the core has exactly two paths.

If either grid dimension is one, every valid route is forced along a single line, so two paths are impossible.

**Core for `k=3`**

The preferred core is a full `2\times3` rectangle when it fits. A route needs two right moves and one down move. Choosing where the one down move occurs gives:

$$
\binom31=3
$$

paths.

If that orientation does not fit but `m\ge3` and `n\ge2`, the source uses a `3\times2` rectangle. It is the transpose and again has three paths.

A grid with both dimensions at most two has at most the two paths of a free `2\times2` grid. Hence rejection for `k=3` outside these cases is necessary.

**Cores for `k=4`**

If a `2\times4` core fits, a route contains three right moves and one down move. The down move can occupy any of four positions, giving:

$$
\binom41=4.
$$

The transposed `4\times2` rectangle works identically.

When neither thin rectangle fits but both dimensions are at least three, the source uses a `3\times3` core with cells `(0,2)` and `(2,0)` blocked.

Its path-count table is:

```text
1  1  #
1  2  2
#  2  4
```

Each free cell's value is the sum from above and left. The core exit therefore receives exactly four paths.

The blocked top-right and bottom-left corners remove the two outermost routes of the fully free `3\times3` grid, which would have six.

**Why the feasibility cases are complete**

An all-free grid has the maximum possible number of right/down paths for fixed dimensions; adding obstacles cannot create more.

For requested values through four:

- one path is always possible;
- at least two paths require both dimensions at least two;
- three paths require a `2\times3` or `3\times2` capacity;
- four paths require one dimension at least four while the other is at least two, or both dimensions at least three.

These are exactly the source's dimension branches. The remaining shapes have all-free maximum below `k`, so returning an empty list is correct.

**Opening the chosen core**

The source loops across `height\times width` and opens every cell except entries in `blocked`.

For all rectangular cores `blocked` is empty. Only the special `3\times3` four-path core uses its two blocked corners.

The core's exit is:

$$
(height-1,width-1).
$$

Every core construction leaves this cell free.

**Building a forced tail**

From the core exit, the source opens the remainder of that row through the final column:

```python
for col in range(exit_col, n):
    grid[exit_row][col] = "."
```

It then opens the final column downward through the last row:

```python
for row in range(exit_row, m):
    grid[row][n - 1] = "."
```

This tail first moves right and then down. At every tail cell there is only one forward free direction:

- before the final column, downward cells outside the core remain blocked;
- in the final column, moving right leaves the grid.

No other core boundary cell receives a connection to the tail. Therefore every complete path must reach the core exit, and every arrival has exactly one way to continue.

When the core already reaches the final column or final row, one corridor part has zero additional length. The same uniqueness reasoning still holds.

**Converting to strings**

The mutable rows make cell assignments easy. The return expression joins each row into the required string while preserving all obstacle and free markers.

The contract accepts any correct grid, so the output need not resemble an example.

**Degenerate dimensions**

For `m=1` or `n=1`, the unique-path core and tail open the single available line. Requests above one are correctly rejected because right/down movement has no branching dimension.

For `m=n=1` and `k=1`, the sole free cell is both endpoints and represents one valid zero-move path.

## Complexity detail

Initializing the full grid writes `mn` cells. Opening a constant-size core and a corridor costs at most `O(m+n)`, and joining all rows writes another `mn` characters. Total time complexity is `O(mn)`.

The mutable grid contains `mn` characters, and the returned strings contain `mn` characters. Peak auxiliary/output storage is `O(mn)`. The `blocked` set contains at most two coordinates and is constant size.

Writing an explicit `m\times n` result already requires `\Omega(mn)` time and output space, so the construction is asymptotically optimal for this interface.

## Alternatives and edge cases

- **Search all obstacle patterns:** There are `2^{mn}` grids. Small fixed cores give the requested counts directly.

- **Open the whole grid:** Its path count is a binomial coefficient and often exceeds `k`. Obstacles are needed to control counts.

- **Dynamic-programming construction search:** DP can count paths in a proposed grid but does not by itself find obstacles efficiently. The source uses DP reasoning only to validate a known core.

- **Attach a branching tail:** Any extra branch after the core would multiply or add paths and destroy the exact count. The source uses a forced corridor.

- **Connect more than one core boundary cell:** That could let paths leave before the designated exit. All non-tail exterior cells remain blocked.

- **`k=1`:** A one-cell core plus the boundary corridor always works.

- **One row or one column with `k>1`:** Only one monotone route can exist, so `[]` is required.

- **`2\times2` with `k=3` or `4`:** The all-free maximum is two, making both requests impossible.

- **`2\times3` with `k=4`:** Its all-free maximum is three, so rejection is correct.

- **`3\times3` with `k=4`:** Blocking the two opposite non-endpoint corners reduces six paths to four.

- **Larger grids:** Only the small top-left core creates choices. Extra dimensions are absorbed by the one-path tail.

- **Core reaches an outer boundary:** Reopening existing exit cells is harmless, and the remaining tail stays unique.

- **Output identity:** Rows are joined into new strings; the mutable grid is not returned directly.

- **Impossible result:** The complete legal parameter sweep confirms every empty result occurs only when even an all-free grid has fewer than `k` paths.
