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

### Required Complexity

- **Time:** $O(R)$
- **Space:** $O(R)$

<details>
<summary>Approach</summary>

#### General

**Find each user's next chronological visit**

Partition rows by `user_id` and order each partition by `visit_date`. The window function `LEAD(visit_date)` attaches the following visit to every row without mixing users. For the last row in each partition, `LEAD` returns `NULL`; replace that missing date with the fixed terminal date `2021-01-01`.

The table's composite primary-key order matches `(user_id, visit_date)`, so an ordered index scan can feed the window operation in one pass. The logic remains correct regardless of the physical order in which fixture rows were supplied.

**Reduce the gaps to one value per user**

Compute the whole-day difference from each `visit_date` to its attached next date. Group these gap rows by `user_id` and take `MAX`. Every true consecutive pair contributes exactly once, and the replacement terminal date contributes exactly one final window per user. Therefore the maximum covers precisely all windows required for that user.

#### Complexity detail

Let $R$ be the visit count and $U$ the user count. Scanning the composite primary-key order, attaching the next date, and updating one maximum per user takes $O(R)$ time. A general window implementation may materialize all $R$ rows, so the conservative space bound is $O(R)$; a streaming ordered implementation needs only $O(U)$ aggregate state.

#### Alternatives and edge cases

- **Self-join every later visit:** joining each row to all later dates and then selecting the nearest can create $O(R^2)$ intermediate pairs.
- **Correlated next-date subquery:** searching the table separately for every visit repeats work unless the optimizer turns it into an ordered scan.
- **Global `LEAD`:** omitting `PARTITION BY user_id` can make another user's visit incorrectly close a window.
- **Unordered window:** omitting `ORDER BY visit_date` follows arbitrary row order rather than chronology.
- **Single visit:** its gap to `2021-01-01` is both its only window and its maximum.
- **Terminal gap wins:** the days after the last recorded visit must compete with all internal gaps.
- **Unsorted fixture rows:** chronological ordering belongs in the query, not in assumptions about input serialization.
- **Leap year:** use date arithmetic so February 29 and all cross-month gaps are counted correctly.
- **Output order:** no row order is required, so fixtures compare the result as an unordered table.

</details>
