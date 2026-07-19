# Consecutive Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 180 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/consecutive-numbers/) |

## Problem Description
### Goal
The `Logs` table records an integer `num` on each row, with `id` defining the chronological sequence. Find values that occur on at least three rows in immediate succession when the records are read by increasing identifier.

Return one column named `ConsecutiveNums` containing each qualifying number once, in any order. A run longer than three rows still contributes only one result value, while separate qualifying runs of the same number must not duplicate it. Equal values separated by a different log row are not consecutive, and mere frequency anywhere in the table is insufficient without a length-three contiguous run.

### Function Contract
**Inputs**

- `Logs(id, num)`: log rows whose id defines sequence order

**Return value**

One column named `ConsecutiveNums` containing each qualifying number once.

### Examples
**Example 1**

- Sequence: `1,1,1,2,1,2,2`
- Output: `1`

**Example 2**

- Sequence: `5,5`
- Output: no rows

**Example 3**

- Sequence: `2,2,2,2`
- Output: one row containing `2`
