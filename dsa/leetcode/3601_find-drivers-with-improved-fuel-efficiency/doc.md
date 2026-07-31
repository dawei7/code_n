# Find Drivers with Improved Fuel Efficiency

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3601 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/find-drivers-with-improved-fuel-efficiency/) |

## Problem Description
### Goal
The `drivers` table identifies drivers, while `trips` records the date, distance traveled, and fuel consumed for every trip. A trip's fuel efficiency is its own `distance_km / fuel_consumed` value. Divide trips by calendar month: January through June belongs to the first half of the year, and July through December belongs to the second half.

For each driver, independently average the per-trip efficiency values in each half. Keep only drivers who have at least one trip in both halves and whose second-half average is strictly greater than their first-half average. The improvement is the unrounded second-half average minus the unrounded first-half average.

Return the driver identity, both half-year averages, and the improvement, rounding each reported measure to two decimal places. Sort larger improvements first; when improvements tie, sort driver names in ascending order.

### Function Contract
**Inputs**

- `drivers`: rows with unique `driver_id` values and their `driver_name`
- `trips`: rows with unique `trip_id`, a `driver_id`, `trip_date`, `distance_km`, and `fuel_consumed`

Every trip references its driver. Fuel consumption is positive, so each efficiency division is defined.

**Return value**

An ordered table with columns `driver_id`, `driver_name`, `first_half_avg`, `second_half_avg`, and `efficiency_improvement`. Include only strictly improving drivers represented in both half-years.

### Examples
**Example 1**

For Alice, first-half trip efficiencies average to `11.97`, while second-half trip efficiencies average to `14.02`, producing `2.05` improvement. Bob improves from `11.24` to `13.33`, producing `2.10` improvement. Bob is listed first because his improvement is larger.

**Example 2**

A driver with trips only from January through June is absent from the result because a second-half average cannot be computed.

**Example 3**

If a driver's averages are `8.50` in both halves, the driver is excluded: the condition requires a strict improvement, not equality.
