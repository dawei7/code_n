## General

**Intervals must be merged independently per hall**

Two events interact only when their `hall_id` values match. Within one hall, events are ordered by `start_day`. Once ordered, overlapping events form consecutive islands: a new island begins only when the next start lies after every end date seen in the current island.

Comparing a row only with the immediately previous row's `end_day` is insufficient. For intervals `[1,10]`, `[2,3]`, and `[9,12]`, the third interval overlaps the first even though it does not overlap the second. The solution therefore carries the maximum end date reached so far.

The query implements the standard gaps-and-islands pattern with three common table expressions.

**CTE `S` computes the running reach**

For every event, `cur_max_end_day` is calculated with

`MAX(end_day) OVER (PARTITION BY hall_id ORDER BY start_day)`.

Partitioning restarts the calculation for each hall. Ordering by `start_day` processes that hall's events chronologically. The running maximum represents the farthest end date covered by the current or any earlier interval in the ordered partition.

This running reach captures chained overlap. Even if an intermediate short interval ends early, an earlier long interval keeps `cur_max_end_day` extended far enough for later overlapping intervals to remain in the same island.

**CTE `T` marks where islands begin**

`LAG(cur_max_end_day)` obtains the running reach associated with the preceding ordered row in the same hall. The current interval overlaps the existing island when

`start_day <= previous_cur_max_end_day`.

Equality is included because events sharing at least one day overlap. For example, an event ending January 14 and another starting January 14 must merge.

The `IF` expression emits zero for an overlap and one for a gap. On the first row of a hall, `LAG` is `NULL`. The comparison with `NULL` is not true, so MySQL's `IF` takes the final branch and marks that row with one, correctly starting the hall's first island.

It is important that `LAG` is applied to the running maximum, not directly to the preceding event's raw end date. That is what preserves transitive overlap.

**CTE `P` turns start markers into group identifiers**

The cumulative window sum

`SUM(start) OVER (PARTITION BY hall_id ORDER BY start_day)`

starts at one for each hall and increases exactly when a gap marker is encountered. Rows connected by direct or chained overlap receive the same `gid`. The numeric identifier itself has no external meaning; only equality within a hall matters.

Partitioning again prevents markers in one hall from changing identifiers in another hall.

**Aggregate each interval island**

The final query groups by `hall_id` and `gid`. Within one overlap island, the merged start is the earliest `start_day` and the merged end is the latest `end_day`, so it selects

`MIN(start_day)` and `MAX(end_day)`.

Every original row belongs to one group. Events in the same group are connected through overlap and must be merged; events in different groups are separated by a genuine date gap and must remain separate.

The temporary `gid` is intentionally omitted from the output, leaving exactly the requested three columns.

**Walk through hall 1**

The first two sample intervals are `[2023-01-13,2023-01-14]` and `[2023-01-14,2023-01-17]`. The first starts a group. The second starts on the prior running maximum date, so its marker is zero and the running reach extends to January 17.

The next interval starts January 18, which is after January 17. Its marker is one, cumulative `gid` increases, and it remains a separate merged event.

Rows from halls 2 and 3 are processed in independent window partitions.

**Duplicates and equal start dates**

The table may contain duplicate rows. Equal intervals necessarily overlap, receive the same island identifier, and collapse under `MIN` and `MAX`.

Multiple events with the same start date also overlap on that date. MySQL's ordered running windows include those peers consistently in the running maximum, and subsequent rows see a reach that covers their maximum end. Their ordering cannot create separate logical islands.

The requested output order is arbitrary, so the final query correctly omits `ORDER BY`.

## Complexity detail

Let $r$ be the number of event rows. Window functions generally require ordering each hall's rows by `start_day`. Across all partitions, sorting dominates at $O(r\log r)$ worst-case time. The window passes and final aggregation are linear after ordering.

The database may materialize common table expressions, sorted partitions, and grouping state using $O(r)$ working space. Exact physical memory and disk use depend on the MySQL execution plan, but $O(r)$ is the appropriate logical auxiliary bound.

Duplicates do not change the asymptotic bounds.

## Alternatives and edge cases

- **Immediate previous end only:** This fails when a long earlier interval bridges over a short nested interval; use the previous running maximum.
- **Recursive interval expansion:** It can merge chains but is more complicated and less natural than window-based gaps and islands.
- **Touching dates:** `start_day == prior maximum end` is overlap because the shared date counts.
- **One-day event:** Its start equals its end and it merges with any same-hall interval containing that date.
- **Different halls:** They never merge even when date ranges are identical.
- **Nested intervals:** The running maximum remains the outer interval's end.
- **Duplicate rows:** Aggregation collapses them without requiring `DISTINCT`.
- **First row per hall:** A `NULL` lag causes the start marker to be one.
- **Transitive overlap:** A chain of pairwise overlaps belongs to one island.
- **Output order:** No ordering clause is required.
