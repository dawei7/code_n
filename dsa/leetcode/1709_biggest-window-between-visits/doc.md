# Biggest Window Between Visits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1709 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/biggest-window-between-visits/) |

## Problem Description
### Goal

The `UserVisits` table records the dates on which users visited a website during 2020. A user's visit window is the number of days from one visit to that user's next visit. The final visit has no later table row, so its window ends on the fixed reporting date `2021-01-01`.

Produce one row per user containing the greatest of these windows. Dates must be compared independently within each user: visits by other users do not end a window, and input row order does not imply chronological order.

### Function Contract
**Inputs**

- `UserVisits(user_id, visit_date)`: one row for each user and visit date
- `(user_id, visit_date)` is unique, and every `visit_date` is during 2020

Let $R$ be the number of rows in `UserVisits`, and let $U$ be the number of distinct users.

**Return value**

A table with columns `user_id` and `biggest_window`, containing each user and the maximum whole-day difference between consecutive visits after appending `2021-01-01` as that user's terminal date. Rows may be returned in any order.

### Examples
**Example 1**

- Input: user `1` visits on `2020-10-20`, `2020-11-28`, and `2020-12-03`
- Output: `(1, 39)`

The consecutive gaps are 39, 5, and 29 days, so the largest is 39.

**Example 2**

- Input: user `2` visits on `2020-10-05` and `2020-12-09`
- Output: `(2, 65)`

The first gap is 65 days and exceeds the 23-day terminal gap.

**Example 3**

- Input: user `3` visits only on `2020-11-11`
- Output: `(3, 51)`

With one recorded visit, its only window ends on `2021-01-01`.
