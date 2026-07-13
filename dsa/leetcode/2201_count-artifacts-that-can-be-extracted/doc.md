# Count Artifacts That Can Be Extracted

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2201 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-artifacts-that-can-be-extracted](https://leetcode.com/problems/count-artifacts-that-can-be-extracted/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-artifacts-that-can-be-extracted/).

### Goal
Count rectangular artifacts whose every occupied cell has been dug from an `n x n` grid. Artifact rectangles do not overlap.

### Function Contract
**Inputs**

- `n`: the grid side length.
- `artifacts`: rectangles `[top_row, left_column, bottom_row, right_column]`, with inclusive bounds.
- `dig`: coordinates of dug cells.

**Return value**

The number of artifacts that can be fully extracted.

### Examples
**Example 1**

- Input: `n = 2`, `artifacts = [[0, 0, 0, 0], [0, 1, 1, 1]]`, `dig = [[0, 0], [0, 1]]`
- Output: `1`

**Example 2**

- Input: `n = 2`, `artifacts = [[0, 0, 0, 0]]`, `dig = [[0, 0], [0, 1]]`
- Output: `1`

**Example 3**

- Input: `n = 3`, `artifacts = [[0, 0, 1, 1]]`, `dig = [[0, 0], [0, 1], [1, 0]]`
- Output: `0`

---

## Solution
### Approach
Store dug coordinates in a hash set. For each artifact, inspect every cell in its inclusive rectangle and count it only if all those coordinates are present. Non-overlap ensures the total artifact area is bounded by the grid area.

### Complexity Analysis
- **Time Complexity**: `O(n^2 + d)`, where `d` is the number of dug cells
- **Space Complexity**: `O(d)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
