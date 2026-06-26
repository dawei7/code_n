# Pascal's Triangle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 118 |
| Difficulty | Easy |
| Topics | Array, Dynamic Programming |
| Official Link | [pascals-triangle](https://leetcode.com/problems/pascals-triangle/) |

## Problem Description & Examples
### Goal
Generate the first `numRows` rows of Pascal's triangle, where each interior value is the sum of the two values above it.

### Function Contract
**Inputs**

- `numRows`: number of rows to generate.

**Return value**

A list of rows, starting with `[1]`.

### Examples
**Example 1**

- Input: `numRows = 5`
- Output: `[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]`

**Example 2**

- Input: `numRows = 1`
- Output: `[[1]]`

**Example 3**

- Input: `numRows = 3`
- Output: `[[1],[1,1],[1,2,1]]`

---

## Underlying Base Algorithm(s)
Dynamic programming from the previous row.

---

## Complexity Analysis
- **Time Complexity**: `O(numRows^2)`
- **Space Complexity**: `O(numRows^2)` for the returned triangle.
