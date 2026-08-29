## General

**Recognize a distinct-item subset-sum problem**

For every positive integer `i`, there is one candidate contribution `i^x`. A representation of `n` chooses some of these contributions, and “unique integers” means each candidate `i` may be selected at most once.

This is a 0-1 subset-sum counting problem. The exact solution uses a two-dimensional table rather than the one-dimensional optimized table named by the Optimal manifest.

**Define the table state**

`f[i][j]` is the number of ways to obtain sum `j` using distinct base integers chosen only from `1, 2, ..., i`.

The row index controls which base values are available; the column is the target sum. By advancing one row per base integer, the recurrence can distinguish “use `i` once” from “do not use `i`.” It never reads from the current row when selecting `i`, so repeated use is impossible.

The table has `n + 1` rows and columns. Bases larger than the integer `n` are not needed: for positive `x`, their powers are certainly greater than `n`. The exact code still iterates all bases through `n` even when their powers become too large.

**Initialize the empty selection**

`f[0][0] = 1` says there is exactly one way to form sum zero using no candidate integers: select nothing.

Every other cell in row zero remains zero because no positive sum can be formed without items. This single base case seeds all later combinations. For example, when a power `i^x` itself equals target `j`, the selection transition reads `f[i - 1][0] = 1` and counts the singleton set `{i}`.

**Two exhaustive choices for each base**

At row `i`, compute `k = i^x`. For every sum `j`:

1. Do not select `i`. Every way counted in `f[i - 1][j]` remains valid, so copy it to `f[i][j]`.
2. Select `i` if `k <= j`. A selection reaching `j` corresponds uniquely to a way of reaching `j - k` from bases below `i`, so add `f[i - 1][j - k]`.

The source expresses this as:

`f[i][j] = f[i - 1][j]`

followed by the optional modular addition.

Because both sources are in row `i - 1`, the chosen base `i` cannot appear twice in one representation.

**Why order is not overcounted**

The problem counts sets of unique integers, not sequences. A representation such as `1^x + 3^x` should count once, not once for choosing 1 then 3 and again for choosing 3 then 1.

The DP considers bases in a fixed increasing order. Each set has exactly one sequence of decisions across rows: skip every absent base and select every present base. There is no second decision order for the same set. That is why the table counts combinations rather than permutations.

**Modulo arithmetic**

When a select transition is possible, the sum of skip and select counts is reduced modulo `10^9 + 7`. Earlier table entries have already been reduced, so copying a skip value preserves a valid modular count.

Modular reduction is safe because only addition is used. For counts `A` and `B`:

$$
(A+B)\bmod M
=
\big((A\bmod M)+(B\bmod M)\big)\bmod M.
$$

The returned `f[n][n]` is therefore the exact number of representations modulo the required modulus.

**A walkthrough with `n = 10` and `x = 2`**

Candidate powers not exceeding ten are 1, 4, and 9.

- Row one can form sums zero and one.
- Row two introduces four. It can extend the sum-one selection to sum five, among other states.
- Row three introduces nine. For target ten, the select transition reads the previous count for sum one, representing `1^2`, and adds `3^2`. This counts set `{1, 3}`.

No other subset of the available squares reaches ten, so the final count is one. Rows for bases four through ten merely copy earlier values because their powers exceed every tracked column.

**Why iterating oversized powers remains correct**

When `k > n`, condition `k <= j` fails for every `j <= n`. The entire row becomes a copy of the previous row. Such a base can never participate in a sum of positive terms totaling `n`, so copying is semantically correct.

It is inefficient compared with breaking once powers exceed `n`, but it does not alter the result.

**Why the recurrence is correct**

Partition all valid subsets of `{1,...,i}` that sum to `j` into two disjoint classes: those excluding `i` and those including it. The first class is counted by `f[i - 1][j]`. Removing `i` from every set in the second class gives a one-to-one correspondence with subsets of earlier bases summing to `j - i^x`. Adding the class counts yields the recurrence.

The initialization is correct for zero available bases, so induction across rows proves every table entry. The requested problem allows bases up to what can fit in `n`, all contained within rows through `n`, making `f[n][n]` the answer.

**The manifest describes a different optimization**

The manifest claims descending one-dimensional DP with `O(n)` space and `O(nm)` time for `m` relevant powers. The exact source allocates `(n+1)^2` cells and scans every row through `n`. Its real time and space are quadratic in `n`.

## Complexity detail

The two nested loops cover `n` base rows and `n + 1` sum columns, performing constant arithmetic per cell. Computing `pow(i, x)` once per row is dominated under the bounded exponent model. Time complexity is `O(n^2)`.

The table contains `(n + 1)^2` Python integers, so auxiliary space is `O(n^2)`. This contradicts the Optimal manifest's `O(n)` claim, which belongs to the editorial's one-dimensional space optimization.

With `n <= 300`, the quadratic table is manageable. Rows for powers greater than `n` still consume time and memory because the exact implementation does not stop early.

## Alternatives and edge cases

- **Descending one-dimensional DP:** Update sums from `n` down to `i^x` so one base is used at most once. It achieves `O(nm)` time and `O(n)` space and matches the manifest.
- **Ascending one-dimensional updates:** This would allow the same power to be reused within one row, violating uniqueness.
- **Top-down memoization:** State `(i, remaining)` expresses the same skip/select recurrence but adds recursion overhead.
- **Power exactly equals `n`:** The singleton representation is counted from `f[i - 1][0]`.
- **Power greater than `n`:** Its row copies the previous row and adds no representation.
- **`x = 1`:** Candidates are the integers themselves; distinct subset sums are still handled by the same recurrence.
- **`n = 1`:** Base one contributes `1^x = 1`, so the singleton set is counted once.
- **No representation:** The target cell remains zero.
- **Several orderings of the same terms:** Fixed row order counts the underlying set only once.
- **Modulo:** It changes stored numeric representatives, not combinatorial validity.
- **Empty set:** It initializes only sum zero and is not returned for positive `n`.
- **Manifest mismatch:** The exact source is two-dimensional and quadratic in both time and storage.
