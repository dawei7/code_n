## General

**Understand the exact query as a rolling-window calculation.** The source first builds common table expression `T`. For every order row, it computes:

`SUM(order_count) OVER (ORDER BY minute ROWS 5 PRECEDING)`.

`ORDER BY minute` places rows into chronological minute order for the window calculation. `ROWS 5 PRECEDING` means the frame contains the current row plus at most five preceding rows: six rows in total once enough history exists. `total_orders` is therefore a rolling six-row sum attached to every minute row.

**The outer query samples interval boundaries.** After every rolling sum exists, the outer query retains only rows satisfying `minute % 6 = 0`. These are minute values six, twelve, eighteen, and so on. At such a boundary, it returns `minute / 6` as `interval_no` and returns that row's rolling `total_orders`.

If the table contains exactly one row for every consecutive minute starting at one, the six rows ending at minute six are minutes one through six, the six ending at twelve are seven through twelve, and so forth. Under that extra condition, sampling the rolling sum at every multiple of six produces the required interval totals.

For the example, the window at minute six contains order counts `0,2,4,6,1,4` and yields seventeen. The window at minute twelve contains `1,2,4,1,4,6` and yields eighteen. Dividing boundary minutes by six produces interval numbers one and two.

**Why the CTE boundary matters.** SQL evaluates the window over all `Orders` rows inside `T` before the outer `WHERE` removes non-boundary minutes. If the filter were applied in the same logical query before calculating the window, only every sixth row would remain and the sum would not represent six minutes. The CTE cleanly separates “calculate for every row” from “report every sixth row.”

**A major row-versus-minute assumption.** `ROWS 5 PRECEDING` counts physical rows, not elapsed minute values. The local reference states that `minute` is a primary key and that total row count is a multiple of six, but it does not state that every minute from one through the maximum is present.

If minutes are missing, the last six rows before a boundary may span more than six minute numbers and cross interval boundaries. If a boundary row such as minute six is missing, the query emits no result for that interval at all. Therefore, under the written reference contract alone, this exact query is not generally correct. It is correct only with an additional consecutive-minute-and-boundary-row guarantee that is not stated.

For instance, rows at minutes `1,2,3,4,5,12` satisfy the primary-key rule and total-row multiple, but the minute-twelve rolling frame sums all six rows and calls it interval two. That mixes minutes from interval one and omits an interval-one output row.

**The requested final ordering is also absent.** The statement requires ascending `interval_no`. The outer query has no `ORDER BY` clause. Ordering inside a window function determines window evaluation, not the guaranteed presentation order of a later SELECT. Many executions may happen to emit ascending rows, but SQL result order is not contractual without an outer `ORDER BY interval_no`. This is a second genuine source defect.

**The manifest describes a different, more robust algorithm.** Directly mapping every minute to its bucket, grouping by that bucket, and sorting the grouped result would follow the reference definition even when minute rows are sparse:

`(minute - 1) DIV 6 + 1`

is the one-based interval number in MySQL. Summing `order_count` per such value handles whichever minute rows actually exist. That is not what the protected query executes, so this approach documents it as an alternative rather than pretending it is the source.

## Complexity detail

Let $M$ be the number of order rows and $I$ the number of emitted boundary rows. The window needs rows in minute order. If the primary-key index can provide that order and the engine streams the frame, processing can be $O(M)$ with a constant six-row rolling state. If an explicit sort is required, time can be $O(M\log M)$ and sort or materialization space can be $O(M)$.

The outer filter is $O(M)$ and emits $I$ rows. The manifest's `O(M + I log I)` time and `O(I)` space correspond to direct bucket aggregation plus output sorting, not this exact unsorted rolling-window query.

## Alternatives and edge cases

- **Direct bucket grouping:** Group by `(minute - 1) DIV 6 + 1`, sum counts, and `ORDER BY interval_no`. This is robust to missing minute rows and matches the manifest.
- **Consecutive minutes:** Only under this unstated guarantee does six preceding rows equal the current six-minute interval.
- **Missing boundary minute:** The exact query omits that interval entirely.
- **Sparse rows:** `ROWS` counts records, not minute distance, so totals can cross interval boundaries.
- **First five rows:** Their rolling frames have fewer than six rows, but they are filtered out when conventional boundaries begin at minute six.
- **Final ordering:** Add outer `ORDER BY interval_no`; window ordering alone does not guarantee result order.
- **Division:** Boundary minutes are divisible by six, so `minute / 6` has an integer value even if MySQL represents it as a decimal type.
- **Primary key:** It guarantees unique minute labels, not consecutiveness.
