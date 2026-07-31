## General

The grid may contain nearly $10^{10}$ different $2 \times 2$ blocks, but at most $10^4$ cells are black. Enumerating the whole grid therefore ignores the useful sparsity in the input. Reverse the viewpoint: determine which blocks each listed black cell changes.

**Map cells to affected blocks**

A black cell at `[row, column]` can belong only to blocks whose top-left row is `row - 1` or `row` and whose top-left column is `column - 1` or `column`. These four combinations include every possible containing block. Discard a combination unless its top-left position satisfies $0 \le r < m-1$ and $0 \le c < n-1$.

Store a hash-map counter keyed by each valid top-left position. Incrementing the counter for every affected block records its exact number of black cells. Because input coordinates are pairwise distinct, no cell can inflate the same block twice.

**Recover the zero-black count**

Every map entry represents one block containing at least one black cell. Place each stored count into the corresponding answer bucket from $1$ through $4$. There are $(m-1)(n-1)$ blocks in total, so subtracting the number of map entries gives the count for bucket $0$. This accounts for the enormous untouched part of the grid without visiting it.

The construction is complete because every nonzero block contains some listed black cell, and processing that cell necessarily reaches the block's top-left position. Its counter is exact because precisely its black cells contribute one increment each.

## Complexity detail

Let $k = \lvert\texttt{coordinates}\rvert$. Each coordinate examines exactly four candidate block positions, and at most $4k$ distinct blocks enter the map. With expected constant-time hash operations, the time complexity is $O(k)$ and the auxiliary space complexity is $O(k)$. Computing the total number of blocks uses constant additional work regardless of $m$ and $n$.

## Alternatives and edge cases

- **Enumerate every block:** Checking all $(m-1)(n-1)$ blocks is correct but costs $O(mn)$ time, which is infeasible when both dimensions approach $10^5$.
- **Store every black cell first:** A set of black coordinates supports block-by-block queries, but still requires enumerating the full grid unless it is combined with the same affected-block insight.
- A black corner belongs to one block, a non-corner boundary cell belongs to at most two, and an interior cell belongs to at most four; the top-left boundary tests handle all three cases uniformly.
- If `coordinates` is empty, the map remains empty and all $(m-1)(n-1)$ blocks correctly fall into bucket $0$.
- The grid may be only $2 \times 2$, in which case exactly one block exists and its count may occupy any bucket from $0$ through $4$.
