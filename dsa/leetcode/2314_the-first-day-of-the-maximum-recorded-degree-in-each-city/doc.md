# The First Day of the Maximum Recorded Degree in Each City

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2314 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/the-first-day-of-the-maximum-recorded-degree-in-each-city/) |

## Problem Description

### Goal

The `Weather` table records an integer degree for a city on a particular calendar day. A city has at most one record per day, and every recorded date is in 2022.

For each city, find its highest recorded degree and report the day on which that maximum first occurred. When multiple records for the city share the maximum degree, select the earliest of those dates. Return the city, chosen day, and degree, with the result rows sorted by `city_id` in ascending order.

### Function Contract

**Inputs**

- `Weather`: A table with integer `city_id`, date `day`, and integer `degree`; `(city_id, day)` is its primary key.

All `day` values belong to the year 2022.

**Return value**

Return one row per city with columns `city_id`, `day`, and `degree`. Choose the row with the greatest degree, breaking ties by the earliest day, and order all result rows by ascending `city_id`.

### Examples

**Example 1**

- Input: `Weather = [(1,"2022-01-07",-12),(1,"2022-03-07",5),(1,"2022-07-07",24),(2,"2022-08-07",37),(2,"2022-08-17",37),(3,"2022-02-07",-7),(3,"2022-12-07",-6)]`
- Output: `[(1,"2022-07-07",24),(2,"2022-08-07",37),(3,"2022-12-07",-6)]`

City 2 reaches 37 twice, so its earlier August date is selected.
