## General

**Aggregate before matching reversed coordinates.** Group the physical rows by
`X, Y` and retain their occurrence counts. This produces one row per distinct
ordered coordinate, preventing duplicate off-diagonal rows from multiplying
the final output during the symmetry join.

Self-join the grouped relation so that the second row's `X` equals the first
row's `Y` and vice versa. For unequal coordinates, keep only
`first_pair.X < first_pair.Y`; the reversed orientation is present in the same
join but is deliberately discarded. For a diagonal coordinate, the join finds
the same grouped row, so additionally require at least two original
occurrences to prove that two physical rows form the symmetric pair.

The grouped relation has exactly one row for each candidate orientation. The
reverse join proves the required partner exists, and the inequality rules
retain exactly one legal orientation. Ordering by both projected columns then
matches the required deterministic result order.

## Complexity detail

Let $R$ be the number of table rows and $D$ the number of distinct ordered
pairs. Hash aggregation and a hash join take expected $O(R+D)$ work. Sorting at
most $D$ output candidates costs $O(D\log D)$, for $O(R+D\log D)$ expected
time. The grouped counts and join structures use $O(D)$ space; physical query
plans and available indexes may change constants.

## Alternatives and edge cases

- **Join raw rows first:** It is correct with careful grouping, but duplicate reverse coordinates can create a quadratic intermediate result before deduplication.
- **Correlated reverse lookup:** Testing `EXISTS` against grouped coordinates is also correct, though a self-join expresses the symmetric relation directly.
- **Single diagonal row:** `(x, x)` alone is not a pair and must be excluded.
- **Repeated diagonal row:** Two or more copies produce one output coordinate.
- **Duplicate off-diagonal rows:** Any positive count in both orientations produces only one result row.
- **Negative coordinates:** The same numeric comparison and reverse-pair logic apply.
- **Output order:** The final `ORDER BY x, y` is required because SQL row order is otherwise unspecified.
