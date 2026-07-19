# Find the Start and End Number of Continuous Ranges

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1285 |
| Difficulty | Medium |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-start-and-end-number-of-continuous-ranges/) |

## Problem Description
### Goal
The `Logs` table records integer log identifiers. Its rows may contain several separated runs: within one run, every identifier is exactly one greater than the preceding identifier, while a missing integer creates a boundary between runs.

Return one row for every maximal continuous range. For each range, report its smallest identifier as `start_id` and its largest identifier as `end_id`. A lone identifier is a valid range whose start and end are equal. Order the result by `start_id`.

### Function Contract
**Inputs**

- `Logs(log_id)`: a table of distinct integer log identifiers.
- Let $n$ be the number of rows in `Logs`, and let $r$ be the number of maximal continuous ranges.

**Return value**

A relation with columns `start_id` and `end_id`, containing exactly the $r$ maximal ranges in ascending `start_id` order.

### Examples
**Example 1**

- Input: `Logs.log_id = [1,2,3,7,8,10]`
- Output: `[[1,3],[7,8],[10,10]]`
- Explanation: The first three identifiers are consecutive, 7 and 8 form the next run, and 10 is isolated.

**Example 2**

- Input: `Logs.log_id = [4,5,6,7]`
- Output: `[[4,7]]`

**Example 3**

- Input: `Logs.log_id = [2,4,8]`
- Output: `[[2,2],[4,4],[8,8]]`
