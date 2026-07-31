# Bikes Last Time Used

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2687 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open problem](https://leetcode.com/problems/bikes-last-time-used/) |

## Problem Description

### Goal

The `Bikes` table records individual rides. Every row has a unique ride identifier, identifies the bike used, and gives valid start and end timestamps for that ride.

For every bike that appears in the table, find the last time it was used. The last-use timestamp is the greatest `end_time` among that bike's rides. Return one row per bike and order the bikes from the most recently used to the least recently used.

### Function Contract

**Input table**

- `Bikes(ride_id, bike_number, start_time, end_time)`: `ride_id` is unique. Each row describes one ride of `bike_number` between two valid datetime values.

**Return value**

Return columns `bike_number` and `end_time`, where `end_time` is that bike's latest ride ending time. Sort the result by `end_time` in descending order.

### Examples

**Example 1**

- Input: Bike `W00576` has rides ending at `2012-03-25 12:40:00`, `2012-03-25 09:10:00`, and `2012-03-28 02:50:00`; bike `W00455` has two rides; bike `W00300` has one.
- Output: `[["W00576","2012-03-28 02:50:00"],["W00455","2012-03-26 17:40:00"],["W00300","2012-03-25 10:50:00"]]`

**Example 2**

- Input: `Bikes = [[1,"A1","2024-01-01 09:00:00","2024-01-01 10:00:00"]]`
- Output: `[["A1","2024-01-01 10:00:00"]]`

**Example 3**

- Input: Two rides of bike `B2` end on consecutive days.
- Output: One row for `B2` containing the later end time.
