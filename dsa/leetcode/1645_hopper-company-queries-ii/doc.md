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
