# Hopper Company Queries III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1651 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/hopper-company-queries-iii/) |

## Problem Description
### Goal
`Drivers` records when drivers joined Hopper. `Rides` records ride requests and their request dates, including requests that were never accepted. `AcceptedRides` identifies the accepted requests and stores each accepted ride's distance and duration.

For every consecutive three-month window wholly contained in 2020, compute the average monthly accepted-ride distance and duration. The first window is January through March and the last is October through December. For each metric, sum all accepted-ride values across the window and divide by 3, including zero for a month with no accepted rides. Round both results to two decimal places.

### Function Contract
**Inputs**

- `Drivers(driver_id, join_date)`: one row per driver. This relation belongs to the shared Hopper schema but does not affect these two ride metrics.
- `Rides(ride_id, user_id, requested_at)`: one row per ride request, keyed by `ride_id`; rejected requests may occur.
- `AcceptedRides(ride_id, driver_id, ride_distance, ride_duration)`: one row per accepted ride, and every `ride_id` refers to `Rides`.
- Let $r$ and $a$ be the row counts of `Rides` and `AcceptedRides`.

**Return value**

Return ten rows with columns `month`, `average_ride_distance`, and `average_ride_duration`. `month` is the starting month number from 1 through 10. Divide each window's total distance and duration by 3, round to two decimal places, and order by `month` ascending.

### Examples
**Example 1**

If January is the only month with an accepted ride and its distance and duration are 30 and 60, the January-starting row is `[1,10.00,20.00]`; every later row is zero.

**Example 2**

If accepted distance totals for January, February, and March are 3, 6, and 9, the first `average_ride_distance` is $(3+6+9)/3=6.00$.

**Example 3**

If December contains one accepted ride with distance 12 and duration 24, it contributes only to the October-starting window, producing `[10,4.00,8.00]` when the other two months are empty.

### Required Complexity
- **Time:** $O(r+a)$
- **Space:** $O(a)$

<details>
<summary>Approach</summary>

#### General

**Construct every month before joining activity.** Generate a twelve-row month relation for calendar year 2020. This fixed spine ensures that a month with no accepted rides has distance and duration totals of zero rather than disappearing from the computation.

**Aggregate accepted rides by request month.** Left join each month to `Rides` through an explicit half-open date interval, then join matching `AcceptedRides` rows by `ride_id`. Summing `ride_distance` and `ride_duration` counts accepted rides only; rejected requests contribute null acceptance values and therefore add nothing. Requests outside 2020 do not match any month interval.

**Combine three consecutive monthly totals.** For a starting month $m$, join the monthly aggregate to months $m+1$ and $m+2$. Add each metric's three totals, divide by 3.0, and round to two decimal places. Requiring both following months naturally limits the output to starts 1 through 10 while preserving all twelve monthly totals as possible window members.

The month aggregation assigns every accepted ride in 2020 to exactly one request month. Each final row then includes exactly the three required aggregates, including explicit zeros, so its two arithmetic means match the contract.

#### Complexity detail

The month spine and ten windows have fixed sizes. With ordinary join and grouping support, associating $r$ requests with $a$ acceptance rows and aggregating them takes $O(r+a)$ time. The join or aggregation can retain up to $O(a)$ accepted-ride state; all calendar and window relations use constant space.

#### Alternatives and edge cases

- **Window functions:** After producing twelve monthly totals, `AVG(...) OVER (ORDER BY month ROWS BETWEEN CURRENT ROW AND 2 FOLLOWING)` expresses the same forward windows. Filter to months 1 through 10 only after computing the windows so November and December remain available to October's frame.
- **Correlated three-month subqueries:** Summing accepted rides separately for each of ten fixed date ranges is correct, but repeats the ride join and obscures the reusable monthly totals.
- **Average accepted rides directly:** `AVG(ride_distance)` would compute a per-ride average, not the required average of monthly totals divided by three.
- Rejected requests have no matching acceptance row and contribute neither distance nor duration.
- The request date, not the driver's join date, determines the month.
- Accepted rides requested before or after 2020 do not enter any window.
- Empty months contribute zero while still occupying one of the three divisor positions.
- Multiple accepted rides in one month are summed before the window divides by 3.
- November and December can contribute to the October window even though neither is an output starting month.

</details>
