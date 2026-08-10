## General

**Calculate by user and date order.** A rolling average must never mix users. Both window expressions use `PARTITION BY user_id`, creating an independent chronological sequence for each user.

`ORDER BY steps_date` places that user's recorded days in ascending calendar order. The primary key `(user_id, steps_date)` guarantees at most one row per user per date, so there are no same-day ordering ties.

**Average the current and two preceding rows.** The expression

`AVG(steps_count) OVER (PARTITION BY user_id ORDER BY steps_date ROWS 2 PRECEDING)`

uses a row frame consisting of the current row and up to two immediately preceding recorded rows. The shorthand `ROWS 2 PRECEDING` means the frame from two rows before through the current row.

`ROUND(..., 2)` rounds this average to two decimal places and names it `rolling_average`.

For the first row of a user, the average contains one record; for the second, two. Those partial averages are computed inside the CTE but must not appear in the final result.

**Row adjacency alone is not enough.** A user may have gaps in dates. Three consecutive recorded rows could be September 2, September 4, and September 5, which are not three consecutive calendar days. The query therefore performs a separate date-continuity check.

**Look two rows back.** `LAG(steps_date, 2)` returns the date two recorded rows before the current one within the same user/date ordering. `DATEDIFF(current_date, that_date) = 2` becomes Boolean column `st`.

If there are fewer than two preceding rows, `LAG` returns null, `DATEDIFF` is null, and the equality is not true.

**Why a two-day difference proves all three days are consecutive.** There are exactly two intervening row steps between the lagged row and current row: lagged, middle, current. Dates within a user are distinct and strictly increasing because of the primary key and ordering.

If current date minus lagged date is exactly two days, the only possible distinct middle calendar date is one day after the lagged date. Therefore, the three recorded rows cover consecutive dates.

This check would be insufficient without the uniqueness and ordering guarantees; here they make it exact.

**Filter complete windows.** The outer query keeps only `WHERE st = 1`. In MySQL, the equality expression evaluates to one for true. Partial frames and date-gapped triples are discarded.

The retained `rolling_average` was computed from exactly those three rows and is therefore the required three-day average.

**Order the final result.** `ORDER BY 1, 2` means ascending by first selected column `user_id` and then second selected column `steps_date`. This fulfills both ordering requirements.
For every user-date row, the AVG window contains the current and previous two recorded values when they exist. The LAG check is true exactly when those three records are three consecutive calendar dates. Thus every output row has a defined required rolling average, and every date with three consecutive records passes the check. Partitioning prevents cross-user data, rounding supplies the requested display, and final sorting orders the rows.

**Two window functions share the same logical order.** MySQL may optimize their common partitioning and sorting, but correctness does not depend on whether the execution engine physically reuses the sort.

**Boolean alias behavior.** `st` can be null, zero, or one. Only one survives the explicit comparison. This is clearer than relying on general truthiness.

## Complexity detail

Let $S$ be the number of `Steps` rows. Window functions generally require ordering rows within user partitions. Without a suitable index supplying that order, sorting costs $O(S\log S)$ in the worst case.

Once ordered, window averages, lag values, filtering, and output projection are $O(S)$. Final ordering matches the same user/date keys and may reuse order or require another sort, leaving the conservative bound $O(S\log S)$.

Window processing and sorting can use $O(S)$ working storage or spill to disk, matching the manifest's $O(S)$ logical space bound. Physical behavior depends on indexes, partition sizes, and MySQL's optimizer.

An index beginning with `(user_id, steps_date)` aligns with both window orders and final ordering.

## Alternatives and edge cases

- **Three-way self-join by exact dates:** Join each row to records one and two days earlier for the same user, then average their counts. It directly enforces calendar adjacency but performs more joins.
- **Calendar range frame:** A date-based range can express time span, but it must also ensure exactly all three daily rows exist; the LAG check is explicit and reliable here.
- **Fewer than three user records:** `LAG(..., 2)` is null, so no output row is produced.
- **Three recorded rows with a gap:** Their date difference exceeds two and the row is filtered out even though the row frame has size three.
- **Exactly three consecutive dates:** The current third date produces the first rolling average.
- **Long consecutive run:** Every date from the third onward receives an overlapping three-day average.
- **Separate users:** Partitioning resets both averaging and lag state.
- **One row per user-date:** The primary key is essential to infer the middle date from the two-day span.
- **Rounding:** `ROUND` occurs after AVG, not on individual step counts.
- **Partial internal averages:** They exist in the CTE but are removed by `st = 1`.
- **Required order:** Ordinal ordering refers to user ID and step date in the outer select list.
