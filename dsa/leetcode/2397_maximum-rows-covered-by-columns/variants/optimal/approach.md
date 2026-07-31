## General

**Represent each row by the columns it requires.** Because $n \le 12$, one
integer bitmask can record every position containing `1` in a row. Bit $j$ is
set exactly when column $j$ must be selected to cover that row. An all-zero
row becomes mask zero, which is correctly a subset of every selection.

**Enumerate only legal selections.** Generate every combination of exactly
$k=\texttt{numSelect}$ column indices and convert it to a selection mask.
This avoids visiting masks with the wrong number of selected columns and
produces exactly $\binom{n}{k}$ candidates.

**Use a subset test for coverage.** A row mask $r$ is covered by a selected
mask $s$ precisely when `r & s == r`: every bit required by the row is present
in the selection. Count the rows satisfying this relation for each candidate
and retain the largest count.

Every legal set of exactly $k$ columns appears once in the combination
enumeration. For each such set, the bitwise test counts exactly its covered
rows, including all-zero rows. Taking the maximum across this complete
candidate set therefore returns the best achievable coverage.

## Complexity detail

Let $m$ and $n$ be the matrix dimensions and let
$k=\texttt{numSelect}$. Building all row masks takes $O(mn)$ time. There are
$\binom{n}{k}$ selections; constructing each selection mask takes $O(k)$ and
testing all row masks takes $O(m)$. Total time is
$O(mn + (m+k)\binom{n}{k})$. The stored row masks use $O(m)$ auxiliary space;
the iterator holds only one $k$-column combination at a time.

## Alternatives and edge cases

- **Enumerate all bitmasks:** Checking all $2^n$ masks and ignoring those whose
  set-bit count is not $k$ is correct but visits unnecessary candidates when
  $\binom{n}{k}$ is much smaller than $2^n$.
- **Backtracking without masks:** Choosing columns recursively and scanning
  matrix cells can express the same search, but repeatedly inspecting row
  entries adds an avoidable factor of $n$.
- **Subset-frequency transform:** Count identical row masks and use a
  subset-sum transform over all $2^n$ masks; this can answer every selection
  mask systematically but is more machinery for the small limits.
- **All-zero rows:** Mask zero satisfies the subset test for every selection
  and must always contribute to the count.
- **Too many ones in one row:** A row with more than $k$ set bits can never be
  covered, which the subset test rejects automatically.
- **Select every column:** When $k=n$, the unique selection covers all $m$
  rows.
- **Duplicate rows:** Equal row masks represent distinct matrix rows and each
  must be counted separately.
