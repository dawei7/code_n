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

### Required Complexity
- **Time:** $O(n \log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**A stable key for one continuous run.** Sort identifiers conceptually by `log_id` and assign `ROW_NUMBER()` values beginning at one. Within a continuous range, both `log_id` and the row number increase by one at each row, so their difference remains constant. When an identifier is missing, `log_id` jumps by more than the row number and the difference changes.

Compute `log_id - ROW_NUMBER() OVER (ORDER BY log_id)` as a range key. Group rows by that key, take `MIN(log_id)` and `MAX(log_id)`, and order the resulting ranges by their starts. Every continuous run has one constant key. Conversely, two adjacent sorted rows with the same key must differ by exactly one, so a group cannot cross a gap. The grouped minima and maxima are therefore precisely the maximal ranges.

#### Complexity detail

For $n$ input rows, the window ordering costs $O(n \log n)$ in the general database execution model. Computing keys and aggregating the groups is linear after ordering. The ordered window and grouped intermediate relation may require $O(n)$ working space; the final result contains $r$ rows.

#### Alternatives and edge cases

- **Start/end anti-joins:** Identify values without predecessors and values without successors, then pair each start with its next end. This is valid but can create an expensive start-by-end join without careful indexing or window functions.
- **User variables:** MySQL session variables can track the preceding identifier, but their evaluation order is less portable and easier to misuse than a window expression.
- **Singleton range:** An identifier with neither consecutive neighbor must produce equal `start_id` and `end_id`.
- **Multiple gaps:** Every missing integer terminates the preceding maximal range, even when the next identifier is much larger.
- **Input order:** Table rows have no inherent order; the window and final result must both specify ordering explicitly.

</details>
