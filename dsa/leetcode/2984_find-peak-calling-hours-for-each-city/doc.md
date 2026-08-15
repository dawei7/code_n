# Find Peak Calling Hours for Each City

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2984 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/find-peak-calling-hours-for-each-city/) |

## Problem Description

### Goal

The `Calls` table records each call's caller, recipient, timestamp, and city.
Its primary key is the combination `(caller_id, recipient_id, call_time)`, so
every row represents one distinct call.

For each city, group calls by the hour of day in which `call_time` falls and
find the greatest call count. Return every hour attaining that maximum; when a
city has a tie, all of its tied peak hours must appear. The result columns are
`city`, `peak_calling_hour`, and `number_of_calls`. Sort first by
`peak_calling_hour` descending and then by `city` descending.

### Function Contract

**Inputs**

- `Calls(caller_id, recipient_id, call_time, city)`: one row per call, with a `datetime` timestamp and city name

Let $R$ be the number of rows in `Calls`.

**Return value**

Return one row for every peak `(city, hour)` pair, including all ties, with its
call count and the required descending ordering.

### Examples

#### Example 1

- **Input:** Houston has three calls during hour `22` and one during `21`; New York has one call during each of hours `13` and `14`.
- **Output:** `[("Houston",22,3),("New York",14,1),("New York",13,1)]`
- **Explanation:** Both New York hours tie for that city's maximum; hour `22` sorts before `14` and `13`.

#### Example 2

- **Input:** One city has calls at `00:05` and `23:55`.
- **Output:** Both hours with count `1`.
- **Explanation:** Calendar dates do not matter; grouping uses the hour of day.

#### Example 3

- **Input:** Two cities share the same peak hour.
- **Output:** Their rows are ordered by city descending within that hour.
