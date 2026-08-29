## General

**Process values from smallest to largest**

Ranks compare cells only within a shared row or column. If a cell has a greater value than an earlier cell in its row or column, its rank must exceed that earlier rank. This suggests assigning ranks in increasing value order, so every strictly smaller value that can constrain the current cell has already been finalized.

The dictionary `d` groups coordinates by matrix value. For each cell `(i,j)` with value `v`, it appends the coordinate to `d[v]`. Sorting the dictionary keys then gives the required increasing value order without sorting all coordinate triples separately.

`row_max[i]` stores the greatest rank already assigned to a strictly smaller processed value in row `i`. `col_max[j]` stores the analogous greatest rank for column `j`. Both arrays begin at zero. If a current cell were isolated from equal-valued complications, its smallest legal rank would be

$$
1+\max(\textit{row\_max}[i],\textit{col\_max}[j]).
$$

The added one makes the rank strictly larger than every smaller value in that row and column, while choosing no unnecessary extra gap.

**Why equal values must be handled as connected groups**

Equal-valued cells in the same row or column must have equal ranks. This equality propagates transitively. If cell A shares a row with equal-valued cell B, and B shares a column with equal-valued cell C, then all three must receive one common rank even if A and C do not directly share a row or column.

On the other hand, two equal values in unrelated rows and columns need not share a rank. They may have different lower-value constraints and can legitimately receive different minimal ranks.

For one value `v`, the source finds exactly these connected groups using a temporary Union-Find over row and column identifiers:

- row `i` uses identifier `i`, from 0 through $m-1$;
- column `j` uses identifier `j + m`, from $m$ through $m+n-1$.

Each occurrence `(i,j)` is viewed as an edge connecting its row node to its column node, so the source calls `uf.union(i, j + m)`. If two equal cells share a row, their column nodes meet through that row. If they share a column, their row nodes meet through that column. Chains of such meetings become one DSU component.

Thus two cells of value `v` belong to the same component exactly when the equality rule forces them to have the same rank.

**Find the strongest lower constraint for each equal-value component**

After all coordinates of `v` have been unioned, `rank` maps each component root to the largest rank already present in any row or column touched by that component.

For every cell `(i,j)` of this value, the source computes its root with `uf.find(i)` and updates:

`rank[root] = max(rank[root], row_max[i], col_max[j])`.

Because `rank` is a `defaultdict(int)`, an unseen component begins with lower bound zero. Scanning every cell in the component takes the maximum across all its row and column constraints. Every equal cell in that component must use one shared rank, so it must exceed all of those lower ranks. The smallest possible shared choice is exactly one plus their maximum.

This gathering pass happens before any current-value rank is written into `row_max` or `col_max`. That separation is important conceptually: cells with the same value should not be treated as strictly smaller than one another.

**Assign one minimal rank to the whole component**

The next pass revisits every coordinate of `v` and performs the chained assignment

`ans[i][j] = row_max[i] = col_max[j] = 1 + rank[uf.find(i)]`.

All cells with the same component root use the same stored lower bound and therefore receive the same rank. The answer matrix records it, and the row and column maxima advance so larger values processed later will be placed above it.

Could this overwrite a larger maximum with a smaller one? For cells of one value, two different components cannot share a row or column: if they did, their equal-valued cells would have been unioned through that shared row or column. Within a component, every assigned rank is identical. Therefore each row or column touched during this value batch receives only its component's one rank, and assignment is safe.

The computed rank is at least 1 because component lower bounds begin at zero. It is exactly one larger than the strongest smaller-value constraint, so it is minimal.

**Reset the reusable Union-Find**

The same `UnionFind(m+n)` object is reused for every distinct matrix value. Connections from different values must never mix: equality components are value-specific.

After finishing `v`, the source calls `reset` on each touched row identifier and column identifier. `reset(x)` makes `x` its own parent and restores its size to one. Some identifiers can be reset more than once because several cells share a row or column, but repeated resetting to the same initial state is harmless.

No Union-Find query occurs during the reset pass. By the time the next value begins, every identifier touched by the previous value has been restored, so the next batch starts with independent singleton row and column nodes. Untouched identifiers were already singletons.

Reusing one structure avoids allocating a fresh pair of arrays for every distinct value while preserving strict isolation between batches.

**A simple matrix trace**

For

`[[1,2],[3,4]]`,

value 1 connects row 0 with column 0. Both maxima are zero, so its rank is 1. Now row 0 and column 0 have maximum rank 1.

Value 2 at `(0,1)` sees row maximum 1 and column maximum 0, so it receives rank 2. Value 3 at `(1,0)` similarly sees column 0 at rank 1 and receives rank 2. Finally, value 4 at `(1,1)` sees rank 2 in both its row and column, so it receives rank 3.

For an all-7 matrix, all occurrences connect through their rows and columns into one component. Its lower bound is zero and every cell receives rank 1.

**Why the complete transformation is correct**

Proceed by increasing value. Assume ranks for all smaller values are valid and minimal, and `row_max` and `col_max` summarize their greatest ranks.

For a current equality component, any legal rank must exceed every smaller-value rank in every row and column occupied by one of its cells. Therefore it must be at least one plus the component maximum collected by `rank`. Assigning exactly that number satisfies all strict inequalities against smaller values.

All equal cells connected through same-row or same-column relations receive the same component rank, satisfying equality. Equal cells in separate components share no row or column, so no equality rule connects them. Larger values have not yet been processed and will later consult the updated maxima, ensuring their ranks are greater.

The assignment is thus legal, and no smaller rank could satisfy the component's strongest prior constraint. Induction over sorted values proves every output relation and the global “as small as possible” requirement.

## Complexity detail

Let $V=mn$ be the number of matrix cells and $K$ the number of distinct values. Grouping coordinates costs $O(V)$ time. Sorting the $K$ keys costs $O(K\log K)$, which is at most $O(V\log V)$.

Each cell participates in a constant number of grouping, union, find, constraint, assignment, and reset operations. Union by size and path compression make DSU operations amortized $O(\alpha(m+n))$. The non-sorting work is $O(V\alpha(m+n))$, so sorting dominates and total time is $O(V\log V)$.

The value dictionary stores every coordinate once, requiring $O(V)$ space. The answer uses $O(V)$ returned storage. The DSU arrays use $O(m+n)$, row and column maxima use $O(m+n)$, and the per-value `rank` dictionary has at most the number of cells in that value group. Total auxiliary and output storage is $O(V)$.

The reset pass can touch the same row or column repeatedly within a value group, but there is one pair of reset calls per cell, so it remains linear across the matrix.

## Alternatives and edge cases

- **Fresh Union-Find per value:** This simplifies reset reasoning but repeatedly allocates $m+n$ arrays. With many distinct values, initialization could become unnecessarily expensive.
- **BFS or DFS on row-column graphs:** For each value, treat occurrences as row-to-column edges and traverse connected components. This has the same high-level $O(V\log V)$ bound when adjacency is built efficiently.
- **Update each equal cell immediately:** This can wrongly let one occurrence of a value raise the rank of another or assign different ranks inside a connected equality group. Component constraints must be gathered before assignment.
- **Sort every cell and ignore equality components:** Equal cells connected transitively can require revising ranks already written. Grouping them first prevents inconsistent assignments.
- **All values distinct:** Every value group has one cell, so each component rank reduces to one plus that cell's current row/column maximum.
- **All values equal:** Row-column unions connect the matrix's equality structure; in a full rectangular matrix all cells form one component and receive rank 1.
- **Equal values in separate components:** They may receive different ranks because no shared row or column imposes equality between them.
- **Negative matrix values:** Dictionary grouping and numeric sorting handle them naturally; ranks themselves still start at 1.
- **One row:** Equal values share a component through that row, and increasing values receive increasing minimal ranks.
- **One column:** The symmetric column behavior applies.
- **Repeated reset calls:** Resetting a touched identifier to itself several times is idempotent and occurs only after all roots for the current value have been used.
- **Column identifier offset:** Using `j + m` keeps all columns distinct from row IDs. Without the offset, an unrelated row and column with the same numeric index would be merged.
- **Union-Find reuse across values:** Resetting is mandatory. Leaving one old parent link would falsely force cells of different values into an equality component.
