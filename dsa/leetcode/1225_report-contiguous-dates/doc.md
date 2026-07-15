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

### Required Complexity

- **Time:** $O(d\log d)$
- **Space:** $O(d)$

<details>
<summary>Approach</summary>

#### General

**Create one state-tagged date stream.** Project `fail_date` as `period_date` with state `failed`, project `success_date` with state `succeeded`, and combine them with `UNION ALL`. Apply the 2019 bounds inside both projections so outside rows never participate in grouping.

**Turn consecutive dates into a stable island key.** Within each state, order dates and assign `ROW_NUMBER()`. For consecutive calendar dates, both the date and row number increase by one, so subtracting that many days from the date produces the same anchor for every row in the run. A gap changes the anchor and begins another island even if the later row has the same state.

**Collapse each maximal island.** Group by the state and derived anchor. The minimum date is `start_date` and the maximum is `end_date`. Ordering those grouped rows by `start_date` interleaves failed and succeeded periods chronologically as required.

The primary keys prevent duplicate dates within either state, and the once-per-day model prevents an ambiguous date from carrying both states. Thus each in-range day contributes to exactly one numbered stream and exactly one maximal island.

#### Complexity detail

Filtering and unioning touch $d$ in-range rows. The state-partitioned window ordering dominates the logical work at $O(d\log d)$; grouping is linear after ordering. The combined, numbered, and grouped intermediate state uses $O(d)$ space. A database engine may select an equivalent indexed physical plan.

#### Alternatives and edge cases

- **Correlated earlier-date count:** Counting prior same-state rows separately for every date reproduces the row number but can take $O(d^2)$ time.
- **Self-join adjacent dates:** It can identify boundaries, but expanding each boundary into an end date is more cumbersome than the gaps-and-islands key.
- **Outside-year rows:** Filter them before numbering so they cannot shift island anchors.
- **One-day island:** Its minimum and maximum dates are equal.
- **Same state separated by a gap:** The changed date-minus-row-number anchor keeps the runs separate.
- **Year boundaries:** Only dates from `2019-01-01` through `2019-12-31`, inclusive, are reported.
- **Final ordering:** Grouped SQL output has no inherent order, so `ORDER BY start_date` is required.

</details>
