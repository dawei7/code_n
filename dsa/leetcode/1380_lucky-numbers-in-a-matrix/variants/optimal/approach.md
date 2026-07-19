## General
**Precompute each column's upper extreme.** Scan all rows to build an array where position `c` stores the maximum value in column `c`.

**Test only row minima.** For each row, find the column containing that row's minimum. The distinct-value guarantee makes this position unique. Compare the candidate with the precomputed maximum for its column, and append it exactly when they are equal.

Every lucky value must be selected because it is its row's minimum and will pass its column comparison. Conversely, every appended candidate has been established as both a row minimum and a column maximum, so no non-lucky value can enter the result.

## Complexity detail
Computing all column maxima and finding every row minimum each inspect $mn$ entries, giving $O(mn)$ time. The column-maxima array uses $O(n)$ space, excluding the returned list.

## Alternatives and edge cases
- **Two extrema sets:** Intersect the set of row minima with the set of column maxima. It is concise and also takes $O(mn)$ time, but stores up to $O(m+n)$ values.
- **Check every cell independently:** Recompute its row minimum and column maximum for each entry. This is correct but takes $O(mn(m+n))$ time.
- **No lucky value:** Return an empty list when no row minimum is also its column maximum.
- **One row:** Its row minimum is lucky because each one-entry column has that same value as its maximum.
- **One column:** Only the column maximum is lucky because every entry is its own row minimum.
- **Distinct values:** There is one minimum per row and one maximum per column, so equality ties need no special treatment.
