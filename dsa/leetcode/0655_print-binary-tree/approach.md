## General

**The matrix size depends on the tree height**

Before any node can be positioned, the algorithm must know the tree's height because height determines both the number of rows and the horizontal spacing.

The helper `height(root)` uses an edge-based height convention:

- an empty tree has height negative one;
- a leaf has height zero;
- any non-null node has one plus the larger height of its children.

Returning negative one for null is what makes a leaf evaluate to `1 + max(-1, -1) = 0` without a separate leaf case.

If the computed height is `h`, the matrix dimensions are:

- `m = h + 1` rows;
- `n = 2 ** (h + 1) - 1` columns.

The row count covers depths zero through `h`. The width reserves a centered location for every possible node of a full tree of that height, together with the blank separation required by the layout.

**Initialize every cell as empty**

The expression `[[""] * n for _ in range(m)]` creates `m` separate row lists, each containing `n` empty strings.

Using a comprehension for the outer list matters in Python. Multiplying one row object by `m` would make all rows aliases of the same list, so writing one node could unexpectedly change several rows. The comprehension creates independent rows.

The matrix starts fully blank. The placement traversal writes only actual nodes, so every unused location automatically retains the required empty string.

**Place the root in the top-row center**

Column indices range from zero through `n - 1`. The middle column is `(n - 1) // 2`. Because `n` is odd, this is an exact center.

The initial call is therefore:

`dfs(root, 0, (n - 1) // 2)`.

Inside `dfs`, a non-null node writes `str(root.val)` into `ans[r][c]`. Converting the integer to text satisfies the string-matrix output contract, including negative values.

**Derive the child offsets**

Suppose a node is placed at row `r` and column `c`. Its children belong on row `r + 1`. The horizontal distance from the parent to either child is:

`2 ** (h - r - 1)`.

Thus:

- the left child column is `c - 2 ** (h - r - 1)`;
- the right child column is `c + 2 ** (h - r - 1)`.

The offset halves on each deeper row. This creates progressively finer positions while keeping subtrees in separate horizontal regions.

For height two, the width is seven. The root is placed at column three. At row zero, the offset is two, so its children use columns one and five. At row one, the offset is one, so possible grandchildren occupy columns zero, two, four, and six.

For height one, the width is three. The root uses column one, and its children use columns zero and two.

**Why the layout does not collide**

Imagine each node owns a horizontal interval containing exactly the columns reserved for its possible subtree. The node sits at the interval midpoint. Its left child's interval is the left half and its right child's interval is the right half, with the child placed at that half's midpoint.

The power-of-two width makes all these midpoints integers. Sibling subtrees receive disjoint intervals, and recursive descendants remain inside their ancestor's interval. Therefore, two distinct tree positions never write the same matrix cell.

Missing children simply return without writing, leaving their entire would-be region blank. Existing descendants cannot occur below a missing parent in a tree, so no placement is lost.

**The placement recursion**

`dfs(root, r, c)` has one base case: if the node is `None`, return immediately. Otherwise:

1. Store the node's string value at its assigned row and column.
2. Recurse on the left child at the next row and left offset.
3. Recurse on the right child at the next row and right offset.

The global `h` is captured by the nested helper, so every call uses spacing derived from the same complete-tree height rather than recomputing a local height.

**A subtle last-row expression**

For a real node on the deepest row `r = h`, both children must be null. The call arguments still evaluate `2 ** (h - r - 1) = 2 ** -1`, producing `0.5` and possibly passing a floating-point column to `dfs(None, ...)`. The helper returns before indexing, so this has no effect on the result.

The behavior is safe under the height invariant, but it is not elegant. Guarding each child before computing its position, or returning immediately when `r == h`, would avoid forming meaningless fractional columns.

**Why the algorithm is correct**

The height helper is correct by structural recursion: a node's deepest edge path is one longer than the deeper child path, with null height negative one.

Given that height, the allocated dimensions match the layout definition. The root call places the root at the exact top center. Assume a node has been placed correctly at `(r, c)`. The recursive calls use exactly the specified next row and symmetric power-of-two offsets, so any existing children are placed correctly. Null children write nothing.

By induction down the tree, every existing node reaches its required cell. Since the matrix began with empty strings and only node cells are written, all other cells remain empty. The returned matrix therefore satisfies every layout rule.

## Complexity detail

Let `R = h + 1` be the row count and `C = 2 ** (h + 1) - 1` be the column count.

Computing height visits each of the `N` nodes once, taking `O(N)` time. Allocating and filling the answer matrix takes `O(R * C)` time. Placement visits each node once in `O(N)` time. The matrix has enough positions for the represented tree, so the output-allocation term dominates, giving total time `O(R * C)`.

The returned matrix itself occupies `O(R * C)` space. Height and placement recursion each use `O(h)` call-stack depth, though they run sequentially rather than nesting together. Including output, the overall space bound remains `O(R * C)`. Excluding output, auxiliary stack space is `O(h)`.

For a skewed tree, `C` grows exponentially with height even though there are few real nodes. This is not inefficiency that the algorithm can avoid while still returning the explicitly required dense matrix; the output itself has that size.

## Alternatives and edge cases

- **Breadth-first placement:** A queue can store each node with its row, column, and interval or offset. It avoids placement recursion but still requires height first and the same `O(R * C)` output.

- **Pass interval boundaries:** Give each recursive call a left and right column and place the node at their midpoint. This can make the geometry intuitive and avoids explicitly writing the power formula at every child.

- **Sparse coordinate output:** A map from coordinates to values would avoid allocating blanks, but it would not satisfy the required dense string-matrix return type.

- **Single-node tree:** Height is zero, dimensions are one by one, and the root value occupies the only cell.

- **Only a left child:** The right half remains blank while the left child is placed at the prescribed offset.

- **Only a right child:** The symmetric left region remains blank.

- **Negative node value:** `str(root.val)` includes the minus sign in one cell; visual character width does not change the matrix coordinate rules.

- **Maximum allowed depth:** The matrix width dominates resource use. The constraint caps depth so the required dense layout remains bounded.

- **Empty root:** The source guarantees at least one node. The exact helpers would produce an empty matrix for `None`, but that behavior is outside the stated contract.

- **Aliased rows:** Writing `[[""] * n] * m` would reuse one row object and corrupt multiple rows at once. The outer comprehension is the correct construction.

- **Local subtree height for offsets:** Recomputing spacing from each child's own height would misalign it relative to the global matrix. Every offset must use the original total `h` and current row.

- **Fractional last-row child columns:** They are passed only to null calls in the exact source. A non-null child below global height `h` would contradict the computed height.

- **Output order:** Rows are naturally top to bottom and columns left to right because coordinates are written into an already indexed matrix.
