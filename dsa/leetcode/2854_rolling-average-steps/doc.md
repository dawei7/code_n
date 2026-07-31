# Rolling Average Steps

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2854 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/rolling-average-steps/) |

## Problem Description

### Goal

The `Steps` table records how many steps each user took on particular calendar dates. For every user and date, consider the three-day period ending on that date: the date itself and the two immediately preceding calendar dates.

Report a rolling average only when the table contains a row for that user on all three consecutive dates. Average those three `steps_count` values and round the result to two decimal places. Dates whose three-day calendar window is incomplete must not appear, even if the user has three earlier observations separated by gaps.

Return `user_id`, the ending `steps_date`, and the computed `rolling_average`, ordered by `user_id` and then `steps_date`, both in ascending order.

### Function Contract

**Inputs**

- `Steps(user_id, steps_count, steps_date)`: one row per user and date, with the recorded step count.

The pair `(user_id, steps_date)` is the table's primary key.

**Return value**

A table with columns `user_id`, `steps_date`, and `rolling_average`. Each row represents a complete three-consecutive-day window ending on `steps_date`; the average is rounded to two decimal places. Rows are sorted by `user_id`, then by `steps_date`, in ascending order.

### Examples

**Example 1**

- Input: user `1` has counts `395`, `499`, `712`, and `576` on September 4 through September 7, 2021.
- Output: rows ending on `2021-09-06` with `535.33` and on `2021-09-07` with `595.67`.

**Example 2**

- Input: one user has observations on `2024-01-01`, `2024-01-03`, and `2024-01-04`.
- Output: no rows, because three observations do not form three consecutive calendar days.

**Example 3**

- Input: user `7` records `1`, `2`, and `2` steps on three consecutive dates.
- Output: the last date has rolling average `1.67`.
