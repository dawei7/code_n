## General

**Create one row for every month of 2020**

The recursive `Months` CTE generates month numbers 1 through 12. It begins at 1 and repeatedly adds one while the current value is below 12.

This calendar is the left side of the monthly aggregation so that months with no rides still exist. Without it, an empty month would vanish and three-month windows would no longer line up with calendar months.

**Aggregate accepted distance and duration by request month**

The `Ride` CTE left joins each generated month to `Rides` when the requested date has that month and year 2020. Placing the year condition in the join preserves calendar rows with no matching 2020 request.

It then left joins `AcceptedRides` by `ride_id`. An unaccepted request has null accepted fields. `COALESCE(ride_distance, 0)` and the corresponding duration expression make that request contribute zero.

Grouping by month produces exactly one row per calendar month. `ride_distance` is the sum of accepted-ride distances requested in that month, and `ride_duration` is the analogous duration total.

The Drivers table is irrelevant to this question because accepted-ride records already contain the measurements being averaged; the result does not filter or group by driver membership.

**The required average is over monthly totals**

For a window starting at month $m$, the problem defines

$$
\frac{D_m+D_{m+1}+D_{m+2}}{3},
$$

where $D_k$ is total accepted ride distance in month $k$. It is not the average distance of individual rides. A month with no accepted rides contributes zero as one of the three monthly terms.

The source applies `AVG(ride_distance)` over a three-row window and similarly for duration, then rounds each result to two decimals.

`LIMIT 10` keeps only ten output rows, corresponding conceptually to starting months January through October. Starts 11 and 12 do not have two following months within 2020 and must be omitted.

**What the window frame intends**

`ROWS BETWEEN CURRENT ROW AND 2 FOLLOWING` asks for the current monthly row and the next two rows. If rows are ordered by month inside the window, this gives exactly the desired three consecutive calendar months. For month 1, it averages January, February, and March; for month 10, October, November, and December.

The outer `ORDER BY month` sorts the final displayed rows in ascending order.

**A material exact-source ordering defect**

The checked-in window clauses do not contain `ORDER BY month` inside `OVER (...)`. SQL does not let an outer `ORDER BY` define the logical ordering used by a window function. Likewise, the `GROUP BY month` inside the CTE does not guarantee its output order.

Therefore `ROWS ... CURRENT ROW AND 2 FOLLOWING` operates in an unspecified row order in the exact query. MySQL may happen to feed Ride rows in month order for a particular execution plan, but the SQL contract does not guarantee it. The final outer ordering can rearrange already-computed averages, but cannot repair windows computed over the wrong row sequence.

The intended and robust expression would be `OVER (ORDER BY month ROWS BETWEEN CURRENT ROW AND 2 FOLLOWING)` for both metrics. This approach document preserves and explains the exact source rather than silently claiming deterministic correctness it does not have.


For every month, the calendar join examines exactly 2020 requests in that month. Accepted measurements are present only when the ride has an AcceptedRides row; all others add zero. Consequently, Ride contains correct monthly totals including explicit zero months.

If the window were ordered by month, each retained starting row would average exactly its total and the following two totals, and rounding would meet the contract. As written, the data preparation and final row selection are correct, but the missing window ordering leaves the mapping from rows to three-month frames unproven.

## Complexity detail

Let $r$ and $a$ be the numbers of Rides and AcceptedRides rows. Generating 12 months is constant work. With indexes on `ride_id` and date access supported by the optimizer, joining and aggregating the relevant rows is logically $O(r+a)$.

The Ride CTE has only 12 rows. Window calculation, final sorting of 12 rows, and limiting to 10 are all constant-sized operations. This gives the manifest's $O(r+a)$ time bound.

Physical working space depends on MySQL's join, grouping, sorting, and CTE-materialization plans. Accepted join data can be $O(a)$, while the final monthly and window state is constant-sized. The manifest's $O(a)$ is a reasonable coarse upper summary rather than a portable guarantee about database memory.

## Alternatives and edge cases

- **Correctly ordered forward window:** Add `ORDER BY month` inside each `OVER` clause. This is the smallest change needed for deterministic three-calendar-month frames.
- **Self-join monthly totals:** Join each start month to totals whose month lies from start through start+2, then divide their sum by three. It is more verbose but makes the window membership explicit.
- **Use `SUM(...) / 3` instead of `AVG`:** With all twelve zero-filled months present, both are equivalent for valid three-row frames.
- **Month with no requests:** The calendar left join preserves it and monthly sums become zero.
- **Requested but unaccepted ride:** Its accepted fields are null and contribute zero.
- **Several accepted rides in one month:** Their distances and durations are summed before the window average.
- **Starting month 10:** Its ordered frame must contain months 10, 11, and 12.
- **Starting months 11 and 12:** They are removed by `LIMIT 10` after final month ordering.
- **Outer ordering is insufficient:** It controls presentation only, not the order used to evaluate an unordered window frame.
- **Rounding:** The source rounds the three-month average, not each monthly total.
- **Drivers table unused:** No driver property is needed to compute totals from accepted rides.
