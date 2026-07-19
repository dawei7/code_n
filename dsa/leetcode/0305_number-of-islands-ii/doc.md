# Number of Islands II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 305 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Union-Find |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-islands-ii/) |

## Problem Description
### Goal
Begin with an $m \times n$ grid in which every cell is water. Process `positions` in order; each operation turns the specified row and column into land. Land cells belong to the same island when connected through horizontal or vertical land neighbors.

After every operation, append the current number of distinct islands to the result. Adding land can create a new island or merge several existing islands into one. If an operation names a cell that is already land, leave the grid and count unchanged but still report that count. Diagonal contact does not connect islands, and no operation removes land.

### Function Contract
**Inputs**

- `m`: the number of grid rows
- `n`: the number of grid columns
- `positions`: land-addition coordinates `[row, column]`; an operation may repeat an existing land cell

**Return value**

A list containing the island count after every operation.

### Examples
**Example 1**

- Input: `m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]]`
- Output: `[1,1,2,3]`

**Example 2**

- Input: `m = 1, n = 1, positions = [[0,0]]`
- Output: `[1]`

**Example 3**

- Input: `m = 2, n = 2, positions = [[0,0],[0,0],[1,1],[0,1]]`
- Output: `[1,1,2,1]`
