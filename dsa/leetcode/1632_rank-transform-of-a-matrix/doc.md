# Rank Transform of a Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1632 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Union-Find, Graph Theory, Topological Sort, Sorting, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [rank-transform-of-a-matrix](https://leetcode.com/problems/rank-transform-of-a-matrix/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/rank-transform-of-a-matrix/).

### Goal
Assign each matrix cell a rank while preserving ordering rules within every row
and column: smaller values must receive smaller ranks, equal connected values
share a rank, and ranks should be as small as possible.

### Function Contract
**Inputs**

- `matrix`: an integer matrix.

**Return value**

The rank-transformed matrix.

### Examples
**Example 1**

- Input: `matrix = [[1, 2], [3, 4]]`
- Output: `[[1, 2], [2, 3]]`

**Example 2**

- Input: `matrix = [[7, 7], [7, 7]]`
- Output: `[[1, 1], [1, 1]]`

**Example 3**

- Input: `matrix = [[20, -21, 14], [-19, 4, 19], [22, -47, 24], [-19, 4, 19]]`
- Output: `[[4, 2, 3], [1, 3, 4], [5, 1, 6], [1, 3, 4]]`

---

## Solution
### Approach
Process values in increasing order. For all cells with the same value, union
cells that share a row or column so equal connected cells are ranked together.
Each component receives rank `1 + max(current row rank, current column rank)`,
then row and column rank trackers are updated.

### Complexity Analysis
- **Time Complexity**: `O(m * n log(m * n))`.
- **Space Complexity**: `O(m * n)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
