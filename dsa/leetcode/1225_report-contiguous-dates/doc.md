# Report Contiguous Dates

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1225 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/report-contiguous-dates/) |

## Problem Description

### Goal

The `Failed` table records days on which an automated task failed, and the `Succeeded` table records days on which it succeeded. Each table has one row per recorded date and uses that date as its primary key. The task runs once per day, so a reported day has one of the two states.

Produce a report for the inclusive calendar interval from `2019-01-01` through `2019-12-31`. Combine consecutive days having the same state into one period. For each period, return its state as `failed` or `succeeded`, its first date, and its last date.

Return the periods ordered by `start_date` in ascending order. Dates outside 2019 must not extend, split, or otherwise affect the reported periods.

### Function Contract

**Input tables**

- `Failed(fail_date)`: `fail_date` is the primary key and identifies a day when the task failed.
- `Succeeded(success_date)`: `success_date` is the primary key and identifies a day when the task succeeded.
- Let $d$ be the number of rows from both tables whose dates fall in 2019.

**Return value**

- One row per maximal same-state run, with columns `period_state`, `start_date`, and `end_date`, ordered by `start_date ASC`.

### Examples

**Example 1**

`Failed`

| fail_date |
|---|
| 2018-12-28 |
| 2018-12-29 |
| 2019-01-04 |
| 2019-01-05 |

`Succeeded`

| success_date |
|---|
| 2018-12-30 |
| 2018-12-31 |
| 2019-01-01 |
| 2019-01-02 |
| 2019-01-03 |
| 2019-01-06 |

Output:

| period_state | start_date | end_date |
|---|---|---|
| succeeded | 2019-01-01 | 2019-01-03 |
| failed | 2019-01-04 | 2019-01-05 |
| succeeded | 2019-01-06 | 2019-01-06 |

**Example 2**

A same-state run covering one day is returned with identical `start_date` and `end_date`.

**Example 3**

Rows dated before `2019-01-01` or after `2019-12-31` are excluded before islands are formed.
