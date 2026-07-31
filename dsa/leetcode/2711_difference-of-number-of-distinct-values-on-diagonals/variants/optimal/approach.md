## General

Every cell belongs to exactly one diagonal identified by the constant difference $r-c$. The result depends only on values before and after that cell along this diagonal, so each diagonal can be processed independently.

**Count the upper-left side.** Start once from every row in the leftmost column and once from every remaining column in the top row. While walking down and right, a set contains precisely the distinct values already passed. Record its size before inserting the current value; this excludes the current cell and gives `leftAbove[r][c]`.

**Count the lower-right side.** Visit the same diagonals in reverse, starting from the rightmost column and bottom row. A fresh set now represents exactly the cells already passed below and to the right. Before inserting the current value, subtract this set's size from the stored upper-left count and take the absolute value.

Each forward and reverse collection of starting points partitions the matrix into diagonals, so every cell is visited exactly once per direction. At each visit the maintained set matches one required side of the current cell. The final subtraction therefore produces the specified answer for every position.

## Complexity detail

Let $m$ and $n$ be the matrix dimensions. The two sweeps each visit all $mn$ cells once, with expected $O(1)$ hash-set operations, for $O(mn)$ time. The returned matrix uses $O(mn)$ space. A set holds at most $\min(m,n)$ values, so auxiliary space beyond the result is $O(\min(m,n))$. The benchmark uses `size` as $mn$ and compares these sweeps with rebuilding both sets separately at every cell.

## Alternatives and edge cases

- **Rebuild two sets per cell:** Walking outward from every position is straightforward and correct, but it repeats work and takes $O(mn\min(m,n))$ time.
- **Prefix and suffix set copies:** Storing a distinct-value set for every diagonal prefix and suffix gives direct lookups, but copying sets can reproduce the slower time bound and consume much more memory.
- **Frequency arrays:** Since values are bounded by $50$, fixed arrays can replace hash sets; they retain linear traversal but require careful reset logic for each diagonal.
- The current cell must be inserted only after its side's count is recorded.
- A one-cell diagonal has empty groups on both sides and therefore contributes zero.
- Duplicate diagonal values count once, even when they appear at several positions.
- Rectangular matrices require starting diagonals from both a border row and a border column without processing the corner twice.

