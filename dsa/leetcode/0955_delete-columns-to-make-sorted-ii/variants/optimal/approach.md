## General

**Rows are compared lexicographically, not column by column**

After deleting the same columns from every string, the resulting row strings must satisfy:

`strs[0] <= strs[1] <= ... <= strs[n - 1]`.

Lexicographic order is decided at the first retained column where two adjacent rows differ. Once one pair has already been placed in the correct strict order by an earlier kept column, later columns cannot reverse that pair's order.

The algorithm tracks exactly which adjacent row pairs have already been resolved.

**Meaning of the state array**

Array `st` has `n - 1` Boolean entries. Entry `st[i]` corresponds to adjacent rows `strs[i]` and `strs[i + 1]`.

- False means all previously kept columns were equal for this pair. Their order is still undecided.
- True means some earlier kept column had `strs[i][j] < strs[i + 1][j]`. Their correct order is permanently established.

Only unresolved pairs can constrain a new column.

**First decide whether a column is forced to be deleted**

For current column `j`, the first inner loop examines unresolved pairs.

If any unresolved pair has:

`strs[i][j] > strs[i + 1][j]`,

keeping this column would make the upper row lexicographically greater than the lower row. Because every earlier kept column tied for this pair, the current column would be their first difference and would prove the wrong order.

No later column could repair that first difference. Therefore, the current column is forced to be deleted.

The algorithm sets `must_del`, breaks, increments `ans`, and does not update any resolution state from a deleted column.

**Why state must not change after deletion**

A deleted character does not participate in the final strings. Even if that column would have distinguished some other pair in the correct direction, that distinction disappears when the column is removed.

Updating `st` from a deleted column would let nonexistent information influence later decisions and could cause an invalid column to be kept.

**When a column is safe to keep**

If no unresolved pair descends, keeping the column cannot violate row order:

- a resolved pair ignores it because an earlier first difference already decided the order;
- an unresolved pair either ties or increases correctly.

The second inner loop marks every unresolved pair with a strict increase as resolved:

`strs[i][j] < strs[i + 1][j]`.

Pairs that tie remain unresolved and must be considered at later columns.

**Trace**

For `["ca", "bb", "ac"]`, all adjacent pairs begin unresolved.

At column zero:

- `c > b` for the first pair, so keeping the column would immediately put the first row after the second.
- The column is deleted, and no state changes.

At column one, characters are `a, b, c`. Both adjacent pairs increase, so the column is kept and both become resolved. The answer is one.

For `["xc", "yb", "za"]`, column zero has `x < y < z`. It resolves every pair immediately. Column one may decrease inside the rows, but all row relationships were already decided by column zero, so no deletion is needed.

**Why the greedy decision is optimal**

Whenever the algorithm deletes a column, at least one unresolved pair would be placed in the wrong order if it were kept. Since earlier kept columns tie for that pair, every valid solution that preserves the current earlier decisions must delete this column. The deletion is forced.

Whenever it keeps a column, no unresolved pair is harmed, and some pairs may become permanently resolved. Keeping it costs nothing and can only reduce future constraints. Deleting a safe column cannot produce a solution with fewer deletions.

By processing columns left to right and making only forced deletions, the algorithm minimizes the total.

## Complexity detail

Let `N` be the number of strings and `M` their common length.

Each of `M` columns performs up to two scans over `N - 1` adjacent pairs. Total time is `O(NM)`.

The resolution array has `N - 1` Booleans, so auxiliary space is `O(N)`.

Early breaks can reduce actual work on forced-deletion columns but do not change the worst-case bound.

## Alternatives and edge cases

- **Delete every individually unsorted column:** That solves the different first problem. Here, a later descending column is harmless for pairs already ordered earlier.
- **Try all column subsets:** It is exponential in `M` and ignores the forced nature of bad first differences.
- **Track complete transformed prefixes:** Comparing rebuilt row strings after every decision uses more memory; resolved adjacent pairs are sufficient.
- **One row:** There are no adjacent pairs, so every column is safe and zero deletions are needed.
- **Identical rows:** Their pair never resolves, but no column descends, so keeping every column is valid.
- **All pairs resolve early:** Later columns cannot affect row order and are all kept.
- **Forced bad column:** One unresolved descending pair is enough to require deletion, regardless of other pairs.
- **Deleted column with useful increases:** Those increases must not update `st` because deleted characters vanish.
- **Equal characters:** They leave an unresolved pair unresolved.
- **Difference from strict sorting:** Equal final rows are allowed, so not every pair needs to become resolved.
