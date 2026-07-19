# Range Addition II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 598 |
| Difficulty | Easy |
| Topics | Array, Math |
| Official Link | [LeetCode](https://leetcode.com/problems/range-addition-ii/) |

## Problem Description
### Goal
Begin with an $m \times n$ matrix `M` whose entries are all `0`. For every operation `[a, b]` in `ops`, increment by one each cell `M[x][y]` satisfying $0 \le x < a$ and $0 \le y < b$; every operation therefore updates a rectangle anchored at the matrix's upper-left corner.

After performing all operations, return the number of cells containing the maximum integer in the matrix. If `ops` is empty, every cell remains tied at the maximum value `0`, so all $m \cdot n$ cells must be counted.

### Function Contract
**Inputs**

- `m: int`: matrix row count
- `n: int`: matrix column count
- `ops: list[list[int]]`: each `[a, b]` increments cells with `0 <= row < a` and `0 <= column < b`

**Return value**

- The number of cells attaining the largest final value

### Examples
**Example 1**

- Input: `m = 3, n = 3, ops = [[2,2],[3,3]]`
- Output: `4`

**Example 2**

- Input: `m = 3, n = 3, ops = []`
- Output: `9`

**Example 3**

- Input: `m = 4, n = 5, ops = [[3,4],[2,5]]`
- Output: `8`
