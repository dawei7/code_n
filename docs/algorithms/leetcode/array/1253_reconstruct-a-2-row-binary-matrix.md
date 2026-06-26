# Reconstruct a 2-Row Binary Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1253 |
| Difficulty | Medium |
| Topics | Array, Greedy, Matrix |
| Official Link | [reconstruct-a-2-row-binary-matrix](https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/) |

## Problem Description & Examples
### Goal
Build a two-row binary matrix whose row sums are `upper` and `lower`, and whose column sums match the given `colsum` array.

### Function Contract
**Inputs**

- `upper`: required sum of the first row.
- `lower`: required sum of the second row.
- `colsum`: required sum for each column, each value being `0`, `1`, or `2`.

**Return value**

A valid two-row binary matrix, or an empty list if impossible.

### Examples
**Example 1**

- Input: `upper = 2`, `lower = 1`, `colsum = [1,1,1]`
- Output: `[[1,1,0],[0,0,1]]`

**Example 2**

- Input: `upper = 2`, `lower = 3`, `colsum = [2,2,1,1]`
- Output: `[]`

**Example 3**

- Input: `upper = 5`, `lower = 5`, `colsum = [2,1,2,0,1,0,1,2,0,1]`
- Output: `[[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]`

---

## Underlying Base Algorithm(s)
Greedy construction.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` for the output.
