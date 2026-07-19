## General
**Use a calendar-month window**

Partition rows by employee and order them by `Month`. For each row, sum salaries over a numeric range from two months before the current month through the current month. A `RANGE` frame expresses calendar distance, so a missing month contributes nothing rather than causing an older recorded row to enter the window.

**Mark the latest row independently**

Compute the greatest month in each employee partition, or equivalently assign descending row numbers. These values must be calculated in the same inner relation as the cumulative salary so all salary rows remain available to the window.

**Filter only after both windows are complete**

In an outer query, discard the row whose month equals the partition maximum. Filtering it before window evaluation could remove data needed for another row's cumulative total in a more general ordering. Finally, apply the required employee-ascending and month-descending order.

**Why every reported total is exact**

The partition prevents salaries from different employees from mixing. The numeric frame contains exactly the existing records whose months satisfy `currentMonth - 2 <= Month <= currentMonth`, which is the requested three-calendar-month interval. The outer maximum-month filter removes exactly one latest row per employee while preserving every earlier computed total.

## Complexity detail
For `R` salary rows, partition ordering costs $O(R \log R)$ time in the general case. Window state and the sorted relation use $O(R)$ working space; database indexes may reduce sorting work.

## Alternatives and edge cases
- **Correlated range sum:** directly sums matching rows for each output month but may rescan the table per row and take $O(R^2)$ time.
- **Self-join on the month interval:** is expressive, though it can create several joined rows per output before aggregation.
- **`ROWS BETWEEN 2 PRECEDING`:** is incorrect when recorded months have gaps because it means two prior rows, not two prior calendar months.
- **Filter latest month before the salary window:** risks changing the rows available to window calculations; compute first and filter outside.
- **Missing months:** contribute zero and do not pull an older month into the three-month interval.
- **Fewer than three months of history:** sum only the existing in-range rows.
- **Single recorded month:** is the employee's latest and produces no output row.
- **Independent employees:** each employee has a separate latest month and rolling total.
- **Required ordering:** sort by `Id` ascending, then `Month` descending.
