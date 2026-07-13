# Cyclically Rotating a Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1914 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Matrix, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [cyclically-rotating-a-grid](https://leetcode.com/problems/cyclically-rotating-a-grid/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/cyclically-rotating-a-grid/).

### Goal
Rotate every rectangular layer of a grid counterclockwise by `k` positions.

### Function Contract
**Inputs**

- `grid`: an `m x n` matrix.
- `k`: the number of cyclic rotations.

**Return value**

Return the grid after rotating each layer.

### Examples
**Example 1**

- Input: `grid = [[40,10],[30,20]], k = 1`
- Output: `[[10,20],[40,30]]`

**Example 2**

- Input: `grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2`
- Output: `[[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]`

**Example 3**

- Input: `grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1`
- Output: `[[2,3,6],[1,5,9],[4,7,8]]`

---

## Solution
### Approach
Process each layer independently. Extract its border values in traversal order, rotate the list by `k % perimeter_length`, then write the values back to the same border cells in the original order.

### Complexity Analysis
- **Time Complexity**: `O(m * n)`
- **Space Complexity**: `O(m * n)` for the result, or `O(perimeter)` extra per layer

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
