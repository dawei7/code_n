## General

**Build a complete month calendar**

The recursive `Month` CTE generates integers 1 through 12. It begins with 1 and repeatedly adds one while the current value is below 12. Starting from this calendar ensures months with no active or working drivers still appear.

**Expand drivers into their active months**

CTE `S` left joins each month to Drivers. A driver matches when the join year is before 2020, or when it is 2020 and the join month is no later than the reporting month.

Thus, a pre-2020 driver appears in all twelve month rows. A driver joining in March 2020 appears from month 3 through 12. A post-2020 driver appears nowhere. Because there is no departure date, membership remains active after joining.

The left join preserves a month even if no driver matches, producing a row with null driver data. This is essential for the required zero percentage.

**Identify accepted rides during 2020**

CTE `T` joins Rides to AcceptedRides using their shared `ride_id` and filters request dates to year 2020. Requested but unaccepted rides have no join match and disappear.

`T` keeps `driver_id` and `requested_at`. It does not aggregate yet because the final numerator needs the number of distinct drivers who worked, not the number of accepted rides.

**Match work to the correct active month**

The final left join connects `S` and `T` when:

- driver IDs match,
- the driver joined no later than the request date,
- the reporting month equals the request month.

The date comparison matters for a driver joining during a month: a ride earlier in that same month must not count as work performed after joining.

One driver may have several accepted rides in a month, producing several joined rows. `COUNT(DISTINCT t.driver_id)` counts that driver once, which matches “working drivers.”

The denominator `COUNT(DISTINCT s.driver_id)` counts all active drivers for the month, also immune to duplication caused by multiple rides.

**Calculate the percentage and handle zero**

The expression multiplies working-driver count by 100, divides by active-driver count, and rounds to two decimals. If no active drivers exist, the denominator is zero and MySQL yields null for the division. `COALESCE(..., 0)` returns the required zero.

Grouping by the first selected column creates one result per month.


For each month, `S` contains exactly drivers who had joined by month end. `T` contains exactly accepted 2020 rides. The join retains a driver's rides only in their request month and only after that driver's join date.

Distinct numerator IDs are therefore precisely active drivers with at least one accepted ride that month. Distinct denominator IDs are precisely active drivers. Their rounded ratio is the requested working percentage, and calendar preservation covers empty months.

The two distinct counts deliberately answer different questions. A driver can contribute once to the denominator merely by being active, but contributes to the numerator only after at least one matching accepted ride reaches the joined row. Because every numerator driver came through `S`, the numerator is automatically a subset of the denominator; the percentage cannot exceed 100 on conforming data.

The exact SQL lacks an `ORDER BY` clause. Although it computes the correct twelve rows as a set, `GROUP BY 1` does not guarantee ascending presentation. Deterministic compliance with the ordering requirement would need `ORDER BY month`; this document records the source behavior without editing it.

## Complexity detail

Let $d$, $r$, and $a$ be row counts for Drivers, Rides, and AcceptedRides. Month generation is constant work. With primary-key indexes, building `T` is logically $O(r+a)$. Expanding Drivers across twelve fixed months is $O(d)$ because twelve is constant.

The final join and distinct aggregation depend on accepted-ride multiplicity but are linear in the produced active-driver/month and ride rows under standard hashing, supporting the manifest's high-level $O(d+r+a)$ bound.

Working storage is database-plan dependent. `T` can contain $O(a)$ accepted rows, `S` can contain up to $12d=O(d)$ rows, and distinct aggregation maintains per-month driver identities. The manifest's $O(a)$ is a coarse summary; physical materialization, indexing, and temporary-table costs are controlled by MySQL.

## Alternatives and edge cases

- **Aggregate one row per working driver and month in `T`:** Grouping there can reduce duplicate ride rows before the final join.
- **Monthly driver counts plus window sums:** Aggregate joiners and use a cumulative window function for active counts, then join monthly working-driver counts.
- **Correlated subqueries per month:** They are readable but may rescan base tables twelve times.
- **Several rides by one driver:** `COUNT(DISTINCT)` counts one working driver, not several rides.
- **Ride before join date in the same month:** The explicit date comparison excludes it.
- **No active drivers:** Division produces null and `COALESCE` returns zero.
- **No accepted rides:** The left join gives no non-null `t.driver_id`, so the numerator is zero.
- **Pre-2020 driver:** Included in every reporting month.
- **Post-2020 driver:** Excluded from every reporting month.
- **Requested but unaccepted ride:** Excluded by the inner join in `T`.
- **Missing ordering:** The exact query has no `ORDER BY`, so row order is not guaranteed despite the contract's ascending requirement.
- **Recursive CTE uses `UNION`:** The generated month values are unique, so duplicate elimination does not change the twelve-row result.
