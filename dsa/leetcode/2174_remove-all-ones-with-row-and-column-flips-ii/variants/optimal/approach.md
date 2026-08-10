## General

The matrix contains at most fifteen cells, so the exact solution treats the complete set of remaining ones as one compact state and performs breadth-first search over those states.

An operation only changes ones to zeros. No zero ever becomes one. Therefore every later state is a subset of the original one-cells, which makes a bitmask a natural representation.

**Flatten the matrix into bits**

Cell `(i, j)` maps to bit position `i * n + j`. The initial `state` sets that bit exactly when `grid[i][j]` is one.

The expression uses a sum of distinct powers of two. Because every cell maps to a unique bit, this is equivalent to combining the bits with bitwise OR. A set bit means the corresponding one is still present; a cleared bit means the cell is zero.

The all-zero matrix is mask zero, so testing `state == 0` checks the goal in constant time.

**Search by number of operations**

The queue starts with the initial mask, and `vis` immediately records it. Variable `ans` is the number of operations used to reach every state in the current queue layer.

The loop processes exactly `len(q)` states before incrementing `ans`. Each generated neighbor differs by one row-and-column clearing operation, so all newly enqueued states belong to the next distance layer.

Breadth-first search visits states in nondecreasing operation count. Consequently, the first time mask zero is removed from the queue, `ans` is the minimum number of operations among all transitions represented by the search.

**Construct the result of choosing a pivot**

For a candidate row `i` and column `j`, the code copies the current mask into `nxt`. It then clears every bit in column `j` using

`nxt &= ~(1 << (r * n + j))`

for all rows `r`. A second loop clears every bit in row `i` for all columns `c`.

Clearing an already-zero bit has no effect, and the pivot's bit may be cleared twice without changing the result. The final `nxt` therefore contains exactly the cells outside the selected row and column that were still one.

If this mask has not appeared before, it is recorded and enqueued. Visiting each mask once prevents cycles and repeated exploration. Although every useful operation is monotone, different pivot sequences can reach the same remaining set, so deduplication saves substantial work.

**Understand the exact pivot check**

The problem permits choosing `(i, j)` only when that cell is currently one. The source checks `grid[i][j] == 0` against the original matrix instead of testing the corresponding bit in `state`. It therefore considers every originally-one cell, even if that particular cell has already been cleared.

This is a relaxed transition rule, but it does not reduce the true minimum. To see why, suppose an originally-one pivot is zero in the current state. Some earlier operation cleared it by clearing either its entire row or its entire column. Since operations never restore ones, at least one of those two lines is now empty.

If both the pivot row and column are empty, the relaxed operation changes nothing, and `vis` prevents the same state from being enqueued again. If the row is empty but the column still contains a one, choose any current one in that column as a legal pivot. That legal operation clears the same nonempty column and also clears another row, so it removes at least everything the relaxed pivot would remove. The symmetric argument applies when the column is empty and the row still contains a one.

Thus every relaxed step at a cleared pivot can be replaced by a legal step that reaches a subset of its next mask in no more operations. Extra clearing can never hurt because the only goal is to remove all ones. All genuinely legal pivots are also originally one and are included by the loops. The relaxed search and the legal problem therefore have the same minimum distance to zero.

**Why zero is always reachable**

If a state is nonzero, at least one current bit is set. Its cell was also one in the original grid, so the loops include it as a candidate pivot. Choosing it is unquestionably legal and clears at least that bit. Repeating this argument strictly reduces the number of remaining ones until the mask becomes zero.

Accordingly, the final `return -1` is only a defensive fallback. Under the stated contract, breadth-first search will find zero.

**Why the first zero layer is globally optimal**

Each path from the initial mask represents a sequence of row-and-column clearings. The construction of `nxt` precisely applies the clearing effect, and the relaxed-pivot argument shows its shortest zero path has the same length as a shortest fully legal path.

Breadth-first search exhausts every state reachable in zero operations, then one operation, then two, and so on. If a solution with fewer than `ans` operations existed, its zero mask would have appeared in an earlier processed layer. Therefore returning at the first zero state gives the required minimum.

For an all-zero input, the initial queue already contains mask zero. The first layer test returns zero before generating any transitions, matching the fact that no operation is needed.

## Complexity detail

Let $K=mn$ be the number of cells and let $P$ be the number of ones in the original grid. Every reachable mask is a subset of those $P$ one-cells, so at most $2^P$ states can be visited.

For each state, the code scans all $K$ cells as possible pivots. For each of the $P$ original-one pivots, it loops through $m$ rows and $n$ columns to clear bits, costing $O(m+n)$. The exact bound is therefore

$$
O\left(2^P\left(K+P(m+n)\right)\right).
$$

Since $P\le K$ and $m+n=O(K)$ for a nonempty matrix, a simple worst-case bound is $O(K^2 2^K)$. This is more conservative than the manifest's $O(K2^K)$ claim because the exact source recomputes every row-and-column clear operation bit by bit. Precomputing one clear mask per pivot would remove the extra $m+n$ factor.

The queue and visited set store at most $2^P$ integer masks, so auxiliary space is $O(2^P)$, or $O(2^K)$ in the worst case. A Python integer holds all at most fifteen bits in constant machine-scale storage for these constraints.

## Alternatives and edge cases

- **Memoized depth-first search:** Recursively try a current one and cache each remaining mask. It explores a similar state graph but needs careful minimization and recursion handling instead of BFS layers.
- **Precomputed clearing masks:** Build the row-and-column bitmask for each pivot once, then calculate `nxt = state & ~clear[pivot]` in constant bitwise time. This supports the manifest's $O(K2^K)$ transition bound.
- **Test the current pivot bit:** Replacing the original-grid check with `state >> position & 1` follows the operation contract directly and avoids needing the relaxed-pivot equivalence argument.
- **Greedy largest immediate clearing:** Removing the most ones now can block no cells, but it still need not minimize the number of overlapping row-and-column operations globally; exhaustive state search is justified by $K\le15$.
- **All zeros:** Initial mask zero returns zero operations immediately.
- **Single one:** Selecting that cell clears it in one operation.
- **Single row:** Any current one pivot clears the entire row, so a nonzero grid needs one operation.
- **Single column:** The symmetric result is also one operation.
- **Duplicate successor states:** Different pivots may clear the same remaining set; `vis` ensures that mask is searched only once.
- **Cleared original pivot:** It may be considered by the exact loops, but it either produces no change or can be dominated by a legal current-one pivot on its remaining nonempty line.
- **Original zero pivot:** It is skipped, and it can never become one because operations only clear cells.
- **Monotonic states:** Every useful transition removes at least one bit, so no solution ever needs to revisit a state with more ones.
- **Input preservation:** The algorithm reads `grid` to build and filter masks but never writes to the matrix.
- **Defensive negative return:** Zero is reachable from every valid input, so `-1` should not occur.
- **Manifest discrepancy:** The stored BFS recomputes row and column bit clearing for every transition, so its exact time bound contains an additional line-length factor.
