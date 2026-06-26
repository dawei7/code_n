# Flip Columns For Maximum Number of Equal Rows

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1072 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Matrix |
| Official Link | [flip-columns-for-maximum-number-of-equal-rows](https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/) |

## Problem Description & Examples
### Goal
Given a binary matrix, you may flip any set of columns. Return the maximum number of rows that can become all equal values within each row.

### Function Contract
**Inputs**

- `matrix`: List[List[int]]

**Return value**

int - maximum number of rows that can be made uniform

### Examples
**Example 1**

- Input: `matrix = [[0, 1], [1, 1]]`
- Output: `1`

**Example 2**

- Input: `matrix = [[0, 1], [1, 0]]`
- Output: `2`

**Example 3**

- Input: `matrix = [[0, 0, 0], [0, 0, 1], [1, 1, 0]]`
- Output: `2`

---

## Underlying Base Algorithm(s)
Pattern normalization and hash counting.

---

## Complexity Analysis
- **Time Complexity**: `O(m * n)`
- **Space Complexity**: `O(m * n)` for stored row patterns
