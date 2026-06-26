# The K Weakest Rows in a Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1337 |
| Difficulty | Easy |
| Topics | Array, Binary Search, Sorting, Heap (Priority Queue), Matrix |
| Official Link | [the-k-weakest-rows-in-a-matrix](https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/) |

## Problem Description & Examples
### Goal
Rows contain soldiers (`1`) before civilians (`0`). Return the indices of the `k` rows with the fewest soldiers, breaking ties by smaller row index.

### Function Contract
**Inputs**

- `mat`: binary matrix with each row sorted from `1`s to `0`s.
- `k`: number of weakest row indices to return.

**Return value**

The `k` weakest row indices.

### Examples
**Example 1**

- Input: `mat = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]`, `k = 3`
- Output: `[2,0,3]`

**Example 2**

- Input: `mat = [[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]]`, `k = 2`
- Output: `[0,2]`

**Example 3**

- Input: `mat = [[0],[1],[0]]`, `k = 2`
- Output: `[0,2]`

---

## Underlying Base Algorithm(s)
Counting and sorting.

---

## Complexity Analysis
- **Time Complexity**: `O(m * n + m log m)`
- **Space Complexity**: `O(m)`
