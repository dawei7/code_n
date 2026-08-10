## General

**Let each recursive call report its number of completions**

`dfs(row)` returns how many valid full boards can be formed after earlier rows have already been assigned. This is a natural tree-counting pattern: a leaf returns 1, an impossible branch returns 0 through an empty sum, and an internal node returns the sum of all child counts.

The recursion assigns exactly one queen to each row, so row conflicts need no marker. Boolean arrays track columns and the two diagonal families attacked by earlier queens.

**Translate board geometry into constant-time lookups**

`cols[i]` represents column `i`. The coordinate sum `row + i` is constant along one diagonal direction, so it indexes `main_diag`. The coordinate difference `row - i` is constant along the other direction; adding `n - 1` changes its range from $[-(n-1),n-1]$ to $[0,2n-2]$, suitable for `anti_diag`.

Both diagonal arrays have `2*n - 1` entries, exactly the number of diagonals of one direction on an $n \times n$ board. A candidate is rejected if any of its three markers is already true.

**Choose and restore one queen**

For a safe column, the source assigns true to the column, sum-diagonal, and difference-diagonal markers in one chained statement. It then calls `dfs(row + 1)` and adds that child's returned count to local `result`.

After the child completes, all three markers are reset to false. This is safe because they were false before the placement, and every deeper recursive call has already restored its own changes. The next loop iteration therefore explores a sibling placement from the exact same parent configuration.

No column path or grid is stored because neither is needed to calculate the count. The markers contain all information required to decide future safety.

**The base case and dead ends**

When `row == n`, one queen has been placed in every row without a marker conflict. That is one valid configuration, so the call returns 1.

At an internal state, `result` begins at zero. If no column is safe, no child call occurs and the function returns zero. If several columns lead to solutions, their returned counts are added. These subtrees are disjoint because they choose different columns in the current row, so summation neither loses nor double-counts configurations.

For $n=4$, most early choices eventually return zero. The two complete arrangements each contribute one through a leaf, and the nested sums carry those contributions back to `dfs(0)`, which returns 2.

**Why the recursion counts every solution once**

Every leaf is sound: recursion depth gives one queen per row, and the marker checks prevent shared columns or diagonals. Conversely, any valid arrangement provides one safe column choice at each row. The loops consider that sequence, so its path reaches a leaf returning 1.

Two different arrangements have different columns in at least one row. Their paths enter different child subtrees at the first such row. Since each subtree's count is added once, every distinct configuration contributes exactly one to the final total.

**An unused variable in the selected source**

The public method creates `result = []` before allocating the marker arrays, but this list is never read, written, or returned. The nested helper has a separate local integer also named `result`; that local shadows the outer name during each call.

The unused outer list has no effect on correctness and occupies only constant space, but it can confuse readers into expecting stored boards. This implementation returns only `dfs(0)` and never materializes a configuration.

**Selected class scope**

There is only one solution class in this package's selected file. Its Boolean-array sizes are derived from `n`, so unlike a fixed-capacity implementation it generalizes naturally as long as recursion depth and runtime remain practical.

## Complexity detail

Let $V$ be the number of partial valid placements reached. Every state loops over all $n$ columns, giving $O(nV)$ candidate-check work. The search has depth $n$, and column uniqueness limits complete column orders to $n!$; diagonal conflicts prune many states.

The manifest and source comment summarize the permutation-like search as $O(n!)$. Counting every rejected candidate test yields the safer broad upper bound $O(n \cdot n!)$. Unlike board-producing N-Queens, a complete leaf returns the integer 1 in constant time, so there is no $n^2$ serialization factor.

The three marker families use $n + 2(2n-1) = O(n)$ Boolean entries. Recursion depth is at most $n$, and scalar local state is constant per frame. Auxiliary space is therefore $O(n)$, matching the manifest. Only one integer is returned, so there is no large output structure.

## Alternatives and edge cases

- **Nonlocal counter:** Increment shared state at each complete placement. It performs the same traversal but makes rollback reasoning separate from count propagation.
- **Bit-mask search:** Compute available columns from occupied masks and extract one low set bit at a time. It reduces marker accesses and candidate scans but is less visually tied to board geometry.
- **Memoization:** Ordinary memoization by row and attack masks may share few states because each placement creates a distinct constraint state; bit-mask recursion is usually more useful than a large cache here.
- **Symmetry pruning:** Mirror first-row placements to reduce search, with special handling for the center of odd-sized boards. It is an optimization, not required for the stated $n \le 9$.
- **`n = 1`:** The only candidate reaches `dfs(1)` and contributes one.
- **No safe choice:** Local `result` remains zero, providing the correct additive identity to the parent.
- **Diagonal extremes:** The shifted difference always remains from 0 through $2n-2$, exactly fitting the array.
- **Unused outer `result`:** It can be removed without changing behavior; it is unrelated to the local integer returned by `dfs`.
- **Input remains unchanged:** All state is newly allocated Boolean lists and recursive integers.
- **Traversal order:** Column order changes only when counts are discovered, not the final total.
