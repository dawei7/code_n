# Find Kth Largest XOR Coordinate Value

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1738 |
| Difficulty | Medium |
| Topics | Array, Divide and Conquer, Bit Manipulation, Sorting, Heap (Priority Queue), Matrix, Prefix Sum, Quickselect |
| Official Link | [find-kth-largest-xor-coordinate-value](https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/) |

## Problem Description & Examples
### Goal
For every coordinate `(i, j)` in a matrix, compute the XOR of all values in the rectangle from `(0, 0)` to `(i, j)`. Return the `k`th largest coordinate XOR value.

### Function Contract
**Inputs**

- `matrix`: a 2D integer matrix.
- `k`: the rank to retrieve in descending order.

**Return value**

Return the `k`th largest prefix-rectangle XOR value.

### Examples
**Example 1**

- Input: `matrix = [[5,2],[1,6]], k = 1`
- Output: `7`

**Example 2**

- Input: `matrix = [[5,2],[1,6]], k = 2`
- Output: `5`

**Example 3**

- Input: `matrix = [[5,2],[1,6]], k = 3`
- Output: `4`

---

## Underlying Base Algorithm(s)
Use a 2D prefix XOR recurrence: `pref[i][j] = matrix[i][j] XOR pref[i-1][j] XOR pref[i][j-1] XOR pref[i-1][j-1]`. Collect each coordinate value and select the `k`th largest by sorting or a size-`k` heap.

---

## Complexity Analysis
- **Time Complexity**: `O(m * n log(m * n))` with sorting
- **Space Complexity**: `O(m * n)`
