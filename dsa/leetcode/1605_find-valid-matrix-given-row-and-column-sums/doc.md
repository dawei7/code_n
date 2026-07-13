# Find Valid Matrix Given Row and Column Sums

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1605 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-valid-matrix-given-row-and-column-sums](https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/).

### Goal
Construct any non-negative matrix whose row sums and column sums match the given
arrays.

### Function Contract
**Inputs**

- `rowSum`: required sum for each row.
- `colSum`: required sum for each column.

**Return value**

Any matrix satisfying all row and column sums.

### Examples
**Example 1**

- Input: `rowSum = [3, 8], colSum = [4, 7]`
- Output: `[[3, 0], [1, 7]]`

**Example 2**

- Input: `rowSum = [5, 7, 10], colSum = [8, 6, 8]`
- Output: `[[5, 0, 0], [3, 4, 0], [0, 2, 8]]`

**Example 3**

- Input: `rowSum = [1, 0], colSum = [1]`
- Output: `[[1], [0]]`

---

## Solution
### Approach
Greedily fill cells from top-left to bottom-right. Put
`min(rowSum[i], colSum[j])` into the current cell, then subtract it from the
remaining row and column requirements. This keeps the total remaining row sum
and column sum equal, so it never blocks completion.

### Complexity Analysis
- **Time Complexity**: `O(m * n)`.
- **Space Complexity**: `O(1)` extra space besides the output matrix.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
