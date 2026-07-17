# Hopper Company Queries II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1645 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/hopper-company-queries-ii/) |

## Problem Description
### Goal
`Drivers` records when each driver joined Hopper. `Rides` records ride requests and their request dates, including requests that were never accepted. `AcceptedRides` identifies accepted requests and the driver who completed each one.

For every month of 2020, calculate the percentage of active drivers who worked during that month. A driver is active in a month if the driver joined by that month's final day. A driver is working in a month if that driver completed at least one accepted ride whose request date falls in the month; multiple accepted rides by the same driver still count that driver once.

If a month has no active drivers, report 0. Round percentages to two decimal places and return all twelve months in ascending numeric order.

### Function Contract
**Inputs**

- `Drivers(driver_id, join_date)`: one row per driver, keyed by `driver_id`.
- `Rides(ride_id, user_id, requested_at)`: one row per requested ride, keyed by `ride_id`.
- `AcceptedRides(ride_id, driver_id, ride_distance, ride_duration)`: one row per accepted ride; every `ride_id` occurs in `Rides`.
- Let $d$, $r$, and $a$ be the respective table row counts.

**Return value**

Return exactly twelve rows with columns `month` and `working_percentage`. For month $m$, the percentage is

$$
100\cdot\frac{\text{distinct drivers with an accepted ride requested in month }m}{\text{drivers who joined by the end of month }m}.
$$

Use 0 when the denominator is zero, round to two decimal places, and order by `month` ascending.

### Examples
**Example 1**

In the official fixture, March has four active drivers and one distinct working driver, so its row is `[3,25.00]`. November has six active drivers and two distinct working drivers, producing `[11,33.33]`.

**Example 2**

With one pre-2020 driver who completes a January ride, January reports `[1,100.00]`; later months report zero working percentage when there are no accepted rides.

**Example 3**

If one driver completes several rides in the same month, that driver contributes only once to the numerator because the statistic counts working drivers, not accepted rides.

### Required Complexity
- **Time:** $O(d+r+a)$
- **Space:** $O(a)$

<details>
<summary>Approach</summary>

#### General

**Generate all twelve months.** A recursive common table expression creates the fixed month spine from 1 through 12. Starting from it ensures that months with no drivers or rides remain present.

**Aggregate distinct working drivers by request month.** Join `AcceptedRides` to `Rides` by `ride_id`, restrict requests to 2020, group by the numeric request month, and count distinct `driver_id` values. The request date controls the month because the acceptance table has no separate completion date. Distinct counting prevents several rides by one driver from inflating the percentage.

**Use the month-end active population as denominator.** For month $m$, count driver rows whose `join_date` is earlier than the first day of month $m+1$. This exclusive cutoff correctly includes every join date in month $m$ and all earlier drivers. Divide the month's working count by that active count, guarding a zero denominator, round, and order the month spine.

The two aggregates match the numerator and denominator definitions independently. Their fixed twelve-month join therefore produces every required month exactly once, including zero-activity months.

#### Complexity detail

The month spine has constant size. With ordinary join and grouping support, the driver relation and the ride/acceptance join require $O(d+r+a)$ total input processing. The accepted-ride grouping can retain up to $O(a)$ state for distinct driver/month combinations; the twelve month rows use constant space.

#### Alternatives and edge cases

- **Count accepted rides:** Counting rows rather than distinct drivers overstates months in which one driver completes multiple rides.
- **Divide by all drivers:** Drivers who join after a month ends are not yet active and must not enter that month's denominator.
- **Group only months with rides:** This omits required zero rows; use a complete month relation and left join.
- Drivers who joined before 2020 are active in every 2020 month.
- A driver joining on a month's last day is active in that month.
- Rejected requests never contribute because they have no `AcceptedRides` row.
- Accepted rides requested outside 2020 do not contribute to any reported month.
- A zero active-driver count produces 0 rather than division by zero.

</details>
