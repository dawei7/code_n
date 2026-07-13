# Report Contiguous Dates

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1225 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [report-contiguous-dates](https://leetcode.com/problems/report-contiguous-dates/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/report-contiguous-dates/).

### Goal
Report contiguous date intervals in 2019 where every day has the same status: either `failed` or `succeeded`.

### Query Contract
**Input tables**

- `Failed(fail_date)`: Dates when the system failed.
- `Succeeded(success_date)`: Dates when the system succeeded.

**Output columns**

- `period_state`
- `start_date`
- `end_date`

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

Dates outside 2019 are ignored before intervals are built.

**Example 3**

A one-day run is returned with the same `start_date` and `end_date`.

---

## Solution
### Approach
Union both tables into one stream of `(state, date)` rows and filter to dates in 2019. Use a window function to assign row numbers inside each state ordered by date. Consecutive dates with the same state share a stable grouping key such as `date - row_number`, so grouping by that key and state yields each interval.

Return each interval ordered by `start_date`.

### Complexity Analysis
- **Time Complexity**: Database dependent; logically dominated by sorting the filtered status rows for the window calculation.
- **Space Complexity**: Database dependent; the intermediate windowed result stores one row per filtered date.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
