## General
The condition concerns adjacency in the log sequence, not total frequency. Ordering the rows by `id`, use `LAG(num, 1)` and `LAG(num, 2)` to attach the previous two values to each current row. A run of length at least three is completed whenever

`num = previous_num AND num = two_rows_back_num`.

For `1, 1, 1, 2, 1, 2, 2`, the third row sees two previous `1`s and qualifies. The later `1` has predecessor `2`, so its overall frequency does not matter. This is why a simple `GROUP BY num HAVING COUNT(*) >= 3` would be wrong.

A run longer than three completes more than one overlapping triple. For `2, 2, 2, 2`, both the third and fourth rows qualify, but the requested result contains `2` only once. Apply `DISTINCT` to the qualifying current values.

It is useful to keep two orderings separate: the `ORDER BY id` inside the window defines which rows are consecutive, while the final relation has no required order unless the contract asks for one. If the schema interprets consecutive as consecutive integer identifiers rather than consecutive rows after sorting, the query must additionally verify the id offsets; this package's contract defines the sequence by id order.

Whenever a row is selected, its value equals the values in the two immediately preceding ordered rows, proving three consecutive occurrences. Conversely, any run of at least three equal values has a third row; at that row both lagged values equal the current value, so the run's number is selected. `DISTINCT` removes only duplicate witnesses from overlapping or separate qualifying runs and never removes the sole representation of a qualifying number. The result therefore contains exactly the requested values.

## Complexity detail
The window operation requires id order, typically $O(n \log n)$ work and up to $O(n)$ sorting/window storage without a supporting index. An index on `id` may allow the engine to stream rows in order, after which lag evaluation is linear with constant-size logical history; physical behavior remains engine-dependent.

## Alternatives and edge cases
- Three self-joins on neighboring ids are portable and explicit, but more verbose and dependent on exact id arithmetic.
- Grouping only by `num` loses adjacency and incorrectly accepts separated occurrences.
- A run of one or two rows does not qualify; runs of four or more still return one distinct value.
- Separate qualifying runs of the same number also produce one result row.
- The first two ordered rows cannot complete a triple because their lag values are absent.
