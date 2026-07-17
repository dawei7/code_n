# Hopper Company Queries I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1635 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/hopper-company-queries-i/) |

## Problem Description
### Goal
`Drivers` records when each driver joined Hopper. `Rides` records every requested ride and its request date, including requests that were never accepted. `AcceptedRides` identifies the accepted subset and associates each accepted ride with a driver plus distance and duration data.

For each of the twelve months of 2020, report how many drivers had joined the company by the end of that month and how many rides requested during that month were accepted. Include months with zero activity. Return `month`, `active_drivers`, and `accepted_rides` in ascending month order.

### Function Contract
**Inputs**

- `Drivers(driver_id, join_date)`: one row per driver, keyed by `driver_id`.
- `Rides(ride_id, user_id, requested_at)`: one row per ride request, keyed by `ride_id`.
- `AcceptedRides(ride_id, driver_id, ride_distance, ride_duration)`: one row per accepted ride; every `ride_id` exists in `Rides`.
- Let $d$, $r$, and $a$ be the row counts of these three tables.

**Return value**

Return exactly twelve rows with `month` from 1 through 12. `active_drivers` counts drivers whose `join_date` is no later than the final day of that month. `accepted_rides` counts accepted rides by the associated `Rides.requested_at` month in 2020. Sort by `month` ascending.

### Examples
**Example 1**

For the official fixture, the monthly rows are:

- Output: `[[1,2,0],[2,3,0],[3,4,1],[4,4,0],[5,5,0],[6,5,1],[7,5,1],[8,5,1],[9,5,0],[10,6,0],[11,6,2],[12,6,1]]`

**Example 2**

If one driver joined before 2020 and one January ride was accepted:

- Output begins with `[1,1,1]` and months 2 through 12 contain one active driver and zero accepted rides.

**Example 3**

If drivers join on January 31, February 1, and December 31, their active totals are 1 in January, 2 from February through November, and 3 in December.

### Required Complexity
- **Time:** $O(d+r+a)$
- **Space:** $O(a)$

<details>
<summary>Approach</summary>

#### General

**Build a complete month spine.** A recursive common table expression generates integers 1 through 12. Starting from this fixed relation guarantees that months with neither rides nor new drivers still appear in the output.

**Count accepted rides by request month.** Join `AcceptedRides` to `Rides` on `ride_id`, restrict `requested_at` to calendar year 2020, and group by its numeric month. This deliberately uses the request date; `AcceptedRides` has no independent acceptance date. Left join those counts onto the month spine and replace missing counts with zero.

**Count drivers through each month end.** For month $m$, count drivers whose `join_date` is earlier than the first day of month $m+1$. The exclusive next-month cutoff includes every date in the current month without depending on month length. Drivers who joined before 2020 remain active in all twelve rows; drivers joining after 2020 appear in none.

The month spine establishes exactly the required output domain. The cutoff predicate counts precisely the drivers present by each month end, while the accepted-rides aggregation counts precisely the accepted requests whose request dates fall in that month. Combining the independent counts by month yields every requested statistic once.

#### Complexity detail

The month spine has constant size 12. With ordinary database join and grouping support, scanning $r$ rides and $a$ acceptance rows takes $O(r+a)$ time, and driver cutoff counts across twelve fixed months take $O(d)$ time because 12 is constant. Total time is $O(d+r+a)$. The accepted-ride grouping can retain up to $O(a)$ join/aggregation state; the month relation is constant-sized.

#### Alternatives and edge cases

- **Group only existing ride months:** This omits months with zero rides and cannot produce the required twelve rows without a calendar relation.
- **Count all requested rides:** Left joining `Rides` without filtering through `AcceptedRides` incorrectly includes rejected requests.
- **Month-name comparisons:** Comparing formatted strings is less direct and can mishandle year boundaries; use explicit date ranges and numeric months.
- Drivers who joined before 2020 count as active starting in January.
- A driver joining on the last day of a month counts in that month.
- Rides outside 2020 do not contribute even when accepted.
- The request date determines the accepted ride's reported month.

</details>
