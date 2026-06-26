# Find the Student that Will Replace the Chalk

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1894 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Simulation, Prefix Sum |
| Official Link | [find-the-student-that-will-replace-the-chalk](https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/) |

## Problem Description & Examples
### Goal
Students use chalk in order and repeat from the start. Given total chalk pieces, find the student who first cannot take their required amount.

### Function Contract
**Inputs**

- `chalk`: chalk required by each student.
- `k`: the initial chalk amount.

**Return value**

Return the index of the student who must replace the chalk.

### Examples
**Example 1**

- Input: `chalk = [5,1,5], k = 22`
- Output: `0`

**Example 2**

- Input: `chalk = [3,4,1,2], k = 25`
- Output: `1`

**Example 3**

- Input: `chalk = [1], k = 0`
- Output: `0`

---

## Underlying Base Algorithm(s)
A full cycle consumes `sum(chalk)`, so reduce `k` modulo that sum. Then scan the students once, subtracting each requirement until the next requirement exceeds the remaining chalk.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
