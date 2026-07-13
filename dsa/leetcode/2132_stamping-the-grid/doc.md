# Stamping the Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2132 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Greedy, Matrix, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [stamping-the-grid](https://leetcode.com/problems/stamping-the-grid/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/stamping-the-grid/).

### Goal
Determine whether rectangular stamps of one fixed size can cover every empty cell in a binary grid. A stamp must stay inside the grid and may not cover an occupied cell; stamps may overlap and any number may be used.

### Function Contract
**Inputs**

- `grid`: a binary matrix where `0` is empty and `1` is occupied.
- `stampHeight`: the stamp's height.
- `stampWidth`: the stamp's width.

**Return value**

`true` if all empty cells can be covered by valid stamp placements; otherwise `false`.

### Examples
**Example 1**

- Input: `grid = [[0, 0], [0, 0]]`, `stampHeight = 2`, `stampWidth = 2`
- Output: `true`

**Example 2**

- Input: `grid = [[0, 1], [0, 0]]`, `stampHeight = 2`, `stampWidth = 2`
- Output: `false`

**Example 3**

- Input: `grid = [[0, 0, 0], [0, 0, 0]]`, `stampHeight = 2`, `stampWidth = 2`
- Output: `true`

---

## Solution
### Approach
Build a two-dimensional prefix sum of occupied cells so each candidate stamp rectangle can be checked in constant time. Mark every valid placement in a two-dimensional difference array, then prefix-sum those marks into coverage counts. The arrangement succeeds exactly when every empty cell has positive coverage.

### Complexity Analysis
- **Time Complexity**: `O(mn)`
- **Space Complexity**: `O(mn)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
