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
