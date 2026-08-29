## General

**Generate all twelve reporting months first**

Months with no drivers joining and no accepted rides must still appear. The recursive `Months` common table expression starts with row 1, then repeatedly selects `month + 1` while the current month is below 12. `UNION ALL` preserves every generated row, producing exactly integers 1 through 12.

Using this complete calendar as the left side of later joins guarantees one reporting group per month. Starting from activity tables instead would omit inactive months.

**Aggregate accepted rides before joining them to drivers**

The `Ride` CTE joins `Rides AS r` to `AcceptedRides AS a` by equal `ride_id`. This inner join retains only requested rides that have an accepted-ride record. The additional condition `YEAR(requested_at) = 2020` restricts them to the reporting year.

The condition is written in the `ON` clause. Because this is an inner join, placing it in `WHERE` would have the same filtering effect.

`MONTH(requested_at) AS month` converts each accepted request date into its 1-through-12 reporting month. `GROUP BY month` then creates one row per month having accepted rides, and `COUNT(1) AS cnt` counts those rides. `ride_id` is unique in both relevant tables, so the join produces at most one row per accepted ride.

Pre-aggregating rides is important. The final query also joins multiple drivers to each month. If raw ride rows and driver rows were joined together before counting, every ride could be repeated once per active driver and both counts could be inflated. Reducing Ride to one count row per month prevents that multiplication.

**Join each driver to every month when that driver is active**

The left join from `Months AS m` to `Drivers AS d` uses this condition:

`(m.month >= MONTH(d.join_date) AND YEAR(d.join_date) = 2020) OR YEAR(d.join_date) < 2020`.

A driver who joined during 2020 is matched to their join month and every later month because `m.month` must be at least the join month. A driver who joined before 2020 matches every month, since they are already active in January. A driver who joined after 2020 satisfies neither branch and is excluded from all 2020 groups.

The schema contains no departure date, so once a driver joins, the driver remains active for every later reporting month. The predicate models “currently with the company by the end of the month” as cumulative membership.

Because this is a left join, a month with no matching active driver still remains as a row with null driver columns. `COUNT(driver_id)` counts only non-null IDs, producing zero for such a month rather than counting the preserved calendar row itself.

**Attach the monthly accepted-ride count**

The already aggregated `Ride` CTE is left joined on equal month. A month with accepted rides receives its `cnt` value. A month absent from Ride gets null, and `COALESCE(r.cnt, 0)` converts that null to the required zero.

Since Ride has at most one row per month, joining it to the repeated driver rows repeats the same `cnt` value across that month's rows. The final `GROUP BY month` collapses those rows. MySQL permits selecting the functionally constant `r.cnt` for the group in this query shape; `COALESCE` then supplies the output value.

The selected columns are named `month`, `active_drivers`, and `accepted_rides` as required.

**A January-to-March trace**

A driver who joined in December 2019 satisfies `YEAR(join_date) < 2020` and appears in January, February, and March. A driver who joined January 13, 2020 satisfies the first branch for every month number at least 1, also appearing in all three. A driver who joined February 16 starts matching at month 2, while a March 8 driver starts at month 3.

Consequently, the active count grows cumulatively. Accepted rides do not accumulate: Ride groups each request only under the month in which it occurred, so March's ride count does not carry into April.

**Why the values are correct**

Months generates the exact twelve reporting keys. For each month $k$, the Drivers join includes precisely drivers with a pre-2020 join year or a 2020 join month no later than $k$. Under the no-departure model, that is exactly the active population at the end of month $k$.

The Ride CTE contains precisely accepted rides requested during 2020 and counts them by their actual request month. Joining that one aggregate to the matching calendar month yields the correct non-cumulative ride count. Left joins and `COALESCE` preserve zero-activity months.

One source-level limitation remains: the contract requires ascending month order, but the checked-in SQL contains no `ORDER BY`. `GROUP BY month` does not guarantee presentation order in SQL, even if MySQL often happens to emit groups in numeric order for a particular plan. The computed twelve rows and values are correct as a set, but deterministic ascending output would require `ORDER BY m.month`. This explanation records that exact implementation behavior without changing the solution.

## Complexity detail

Let $d$, $r$, and $a$ be the row counts of Drivers, Rides, and AcceptedRides. Months always has 12 rows, so its recursive generation is constant work.

With indexes on the ride primary keys, joining accepted rides to their requests and aggregating qualifying rows is logically $O(r+a)$, subject to the optimizer's chosen access path. Joining Drivers against 12 fixed months evaluates at most a constant multiple of $d$ candidate month relationships, so it is $O(d)$. The final grouping has only 12 keys. This supports the manifest's high-level $O(d+r+a)$ time bound.

Ride stores at most 12 monthly aggregate rows. The driver-month join can logically produce up to $12d$ rows, which is $O(d)$ because 12 is fixed; a database may stream or materialize them. The manifest's `O(a)` space is a coarse engine-dependent summary, while portable SQL cannot guarantee a specific working-memory plan. The returned result itself is exactly 12 rows.

Date functions, join indexes, hash versus sort aggregation, CTE materialization, and scalar memory use are controlled by MySQL's optimizer, so physical costs can differ from the logical model.

## Alternatives and edge cases

- **Hard-code twelve rows with `UNION ALL`:** This avoids recursion but is verbose. The recursive CTE expresses the calendar range compactly.
- **Aggregate drivers by join month and use a cumulative window sum:** Count pre-2020 drivers into January, count 2020 joiners by month, fill missing months, and run `SUM(...) OVER (ORDER BY month)`. This avoids the range join.
- **Correlated count subqueries per month:** For each of twelve months, count eligible drivers and accepted rides. It is readable but may rescan base tables repeatedly.
- **Join raw rides and raw drivers together:** This creates a many-to-many multiplication within each month and makes simple counts wrong. Pre-aggregating Ride avoids it.
- **Driver joined before 2020:** The OR branch includes that driver in all twelve months.
- **Driver joined during 2020:** The month comparison includes the join month itself because statistics are measured by month end.
- **Driver joined after 2020:** Neither predicate branch matches, so the driver is excluded.
- **Ride requested outside 2020:** The Ride CTE filters it out even if it was accepted.
- **Requested but not accepted:** It has no AcceptedRides match and is excluded by the inner join.
- **Month with no accepted rides:** The left join yields null and `COALESCE` returns zero.
- **Month with no active drivers:** `COUNT(driver_id)` ignores the null from the calendar-preserving left join and returns zero.
- **Ordering requirement:** The exact source lacks `ORDER BY`, so ascending presentation is not guaranteed. Grouping alone must not be relied upon as an ordering contract.
- **Grouping name resolution:** The source writes `GROUP BY month` rather than `GROUP BY m.month`. In this select scope the intended key is the output month; qualifying it would make the intent more robust.
