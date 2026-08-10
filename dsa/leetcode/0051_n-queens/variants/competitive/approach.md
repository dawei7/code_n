## General

**One recursion level represents one row**

`dfs(row)` chooses a column for the queen in `row`. Earlier recursive levels have already placed one queen in each earlier row, so row conflicts are impossible by construction. `curr` stores those selected column indices in row order: `curr[r]` is the queen column for row `r`.

The candidate loop tries every column `i`. It proceeds only if that column and the cell's two diagonals are unused. This turns an apparently two-dimensional attack test into three constant-time Boolean lookups.

**Column and diagonal identifiers**

`cols[i]` marks whether any earlier queen uses column `i`. A top-right-to-bottom-left diagonal has constant `row + i`, so `main_diag[row+i]` represents it. The largest sum is $2n-2$, fitting the allocated `2*n-1` entries.

A top-left-to-bottom-right diagonal has constant `row - i`, ranging from $-(n-1)$ through $n-1$. Adding `n - 1` shifts this into indices 0 through $2n-2$, which are stored in `anti_diag[row-i+(n-1)]`.

The names “main” and “anti” can vary between explanations; correctness depends on the invariant that equal coordinate sums or equal coordinate differences identify the same diagonal.

**Choose, explore, and undo**

For a safe cell, the source sets its column and both diagonal entries to `True`, appends its column to `curr`, and recurses to `row + 1`. These markers ensure every descendant rejects attacks from the new queen.

When the recursive call returns, `curr.pop()` removes the row's column and all three markers are reset to `False`. Restoration is exact because a safe placement was the only active queen using those lines; no descendant remains active after its call has returned.

This rollback allows the loop to try a different column for the same row without contamination from the previous branch. If no candidate is safe, the function simply returns, which tells the preceding row to reconsider its choice.

**Turning a column path into a board**

At `row == n`, `curr` has one column for every row. For a column value `x`, the expression `'.'*x + "Q" + '.'*(n-x-1)` creates a length-$n$ row with one queen in column `x`. Mapping that expression over `curr` creates the board representation.

Under the Python 2 behavior targeted by this older source, `map` eagerly returns a list of row strings, so appending it gives the required `List[str]` board. Each leaf is independent because all rows are materialized before `curr` is later popped.

**A serious Python 3 behavior difference**

In Python 3, `map(...)` returns a lazy iterator rather than a list. The exact source appends that map object directly to `result`, violating the required `List[List[str]]` shape. More seriously, the iterator is tied to the shared mutable `curr` list. Backtracking empties and reuses `curr` before a caller consumes those iterators, so they may yield no rows or otherwise fail to represent the leaf that created them.

The intended Python 3 construction would eagerly materialize the rows, for example with a list comprehension or `list(map(...))`. The protected source is not modified here. Its backtracking algorithm is explained under intended eager-map semantics, while its exact Python 3 return behavior is documented as incompatible.

**Why conflict markers are sufficient**

Queens attack only in rows, columns, and diagonals. Rows are unique by recursion depth. Columns are unique because `cols[i]` must be false before placement. Two cells share one diagonal direction exactly when their coordinate sums match and the other direction exactly when their differences match, so the diagonal arrays exclude every remaining attack type.

When a leaf is reached, all $n$ queens are therefore mutually non-attacking. Conversely, any valid solution selects one safe column in each row. The loops try that sequence, because none of its prefixes conflicts, so every solution has a search path.

Two different paths first choose different columns in some row and therefore create different board strings in that row. No solution is duplicated.

**Selected class versus the alternative**

`Solution2` in the same file uses copied lists of columns, sums, and differences and returns boards through an eager outer list comprehension. The harness selects class `Solution`, whose Boolean-array backtracking and Python-version caveat are the subject of this document.

## Complexity detail

Let $V$ be the number of partial placements visited and $S$ the number of valid solutions. Each state loops over $n$ columns with constant-time conflict checks, for $O(nV)$ search work. Column uniqueness gives $V=O(n!)$ as a conventional coarse bound.

Under intended eager-map semantics, every solution builds $n$ strings of length $n$, costing $\Theta(n^2)$ time and space in the output. A precise output-sensitive time bound is $O(nV + Sn^2)$, and a broad worst-case bound is $O(n^2 n!)$. The source comment records this broader form, while the manifest's $O(n!)$ is a simplified search-only description.

The active path, recursion stack, column array, and two diagonal arrays all use $O(n)$ auxiliary space. Intended eager result storage is $\Theta(Sn^2)$ and is excluded from that auxiliary bound. Under Python 3, lazy map objects change when construction work occurs but do not satisfy the output contract, so their lower immediate storage is not a valid implementation advantage.

## Alternatives and edge cases

- **Eager list comprehension at the leaf:** It preserves this exact search while producing the required Python 3 board lists safely.
- **Full mutable grid:** Write and erase `Q` characters during recursion. It makes board state visual but increases active storage to $O(n^2)$.
- **Bit masks:** Encode used lines in integers and enumerate available columns through bit operations. This often gives the fastest solver but requires careful masking and diagonal shifts.
- **Copied sets or lists per call:** Immutable-style state avoids rollback bugs, but copying on every recursion edge increases allocation.
- **`n = 1`:** One safe column reaches a leaf and should produce `[["Q"]]` under eager construction.
- **No safe column:** The frame returns without appending a board, and its parent restores the preceding queen.
- **Diagonal array boundaries:** `row+i` and `row-i+n-1` both remain within 0 through $2n-2$.
- **Python 3 `map`:** The returned map object is lazy and observes a path later changed by backtracking. The source is not contract-correct unchanged in Python 3.
- **Python 2 intended runtime:** `map` is eager, so the same expression produces stable lists as the author expected.
- **Return ordering:** Increasing column trials determine a depth-first order that the problem does not require.
