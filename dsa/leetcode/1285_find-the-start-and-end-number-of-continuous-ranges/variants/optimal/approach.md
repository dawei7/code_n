## General

**Detect where a new continuous range begins**

Because `log_id` values are unique, sorting them reveals maximal runs of consecutive integers. A row continues the previous range exactly when its identifier is one greater than the preceding identifier.

The innermost query uses `LAG(log_id) OVER (ORDER BY log_id)` to retrieve the preceding sorted value. It computes `delta` as zero when the difference equals one and one otherwise:

`IF((log_id - LAG(...)) = 1, 0, 1)`.

For the first sorted row, `LAG` returns `NULL`. Arithmetic and comparison with `NULL` produce `NULL`, and MySQL's `IF` treats that condition as not true, selecting one. Therefore the first row correctly starts range number one.

For identifiers `1,2,3,7,8,10`, delta values are `1,0,0,1,0,1`. A one marks each gap boundary.

**Turn boundary markers into a stable group identifier**

The next query level computes the running sum

`SUM(delta) OVER (ORDER BY log_id) AS pid`.

Within consecutive rows, delta is zero, so the cumulative value stays unchanged. At a gap, delta one increments it. All identifiers in one maximal continuous range therefore share one `pid`, while different ranges have different values.

The window operations are separated into nested queries because the cumulative sum consumes the result of `LAG`; SQL window functions generally cannot be nested directly in one expression at the same query level.

For the example, cumulative identifiers are `1,1,1,2,2,3`, assigning the expected three groups.

**Collapse each group to its endpoints**

The outer query groups by `pid`. Since every group contains a sorted consecutive run, its smallest `log_id` is the range start and its largest is the range end. `MIN(log_id) AS start_id` and `MAX(log_id) AS end_id` produce exactly those endpoints.

A one-element range has identical minimum and maximum, correctly returning the same start and end.

**Why the grouping is exact**

If two adjacent sorted identifiers differ by one, no gap lies between them and delta zero preserves their group. By transitivity, every chain of consecutive identifiers shares a `pid`. If a difference is greater than one, delta one changes the cumulative sum, so values across that missing region cannot share a group.

Thus each `pid` represents one maximal range: it contains only consecutive identifiers, cannot be extended across either boundary, and covers every input row exactly once. Minimum and maximum are its correct endpoints.

If `Logs` is empty, both window stages and the final grouping produce no rows. That is the natural representation of having no continuous ranges; no fabricated zero or null range is introduced.

**The exact query does not guarantee the requested final order**

The problem explicitly requires ascending `start_id`. The shipped source ends with `GROUP BY pid` and has no outer `ORDER BY`. Although `pid` was created in ascending identifier order and MySQL may often emit groups that way for a particular plan, SQL does not guarantee result order without `ORDER BY`.

The range-detection algorithm is correct, but strict contract compliance would require appending `ORDER BY start_id`, or equivalently ordering by `MIN(log_id)`. This documentation does not pretend that grouping order is a formal substitute for ordering.

## Complexity detail

Let $n$ be the number of log rows. Both window functions require `log_id` order. Without a supporting execution order, sorting costs $O(n\log n)$ time. Window scans and final aggregation are linear after ordering, so total time is $O(n\log n)$.

Window results, sort buffers, the CTE, and groups may require $O(n)$ logical working space. A database can stream or spill portions depending on its plan, but the manifest's $O(n)$ space is a reasonable upper bound for intermediate state.

The final output has $r\le n$ range rows. Adding the missing contractual order would sort at most $r$ rows, still within $O(n\log n)$ time.

## Alternatives and edge cases

- **`log_id - ROW_NUMBER()` grouping:** For consecutive values, subtracting their sorted row number remains constant. Grouping by that difference is a compact islands-and-gaps technique.
- **Recursive range construction:** It is more complex and unnecessary when window functions are available.
- **Single identifier:** Delta starts at one, one group forms, and start equals end.
- **All identifiers consecutive:** The cumulative group identifier never changes after the first row, producing one range.
- **Every pair separated:** Every delta is one, so each identifier becomes a singleton range.
- **Negative or nonstarting identifiers:** Only differences matter; the logic does not require IDs to start at one.
- **Unique-value guarantee:** Duplicate identifiers would produce difference zero and require a clarified meaning, but the schema excludes them.
- **First-row null:** MySQL `IF` selects the else branch for the null comparison, correctly marking a new group.
- **Missing final ordering:** Add `ORDER BY start_id` for a result whose required order is guaranteed rather than incidental.
- **Window sort reuse:** An optimizer may reuse ordering between window stages, affecting constants but not the worst-case bound.
