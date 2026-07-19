# Diagonal Traverse II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1424 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/diagonal-traverse-ii/) |

## Problem Description

### Goal

The nested array `nums` contains nonempty rows that may have different lengths. Treat each value as occupying coordinate `(row, column)`. Values whose coordinate sum `row + column` is equal belong to the same diagonal.

Return all values by increasing diagonal sum. Within one diagonal, visit values from the largest row index to the smallest row index, which moves upward and to the right through the jagged structure.

### Function Contract

**Inputs**

- `nums`: a list of nonempty integer rows.
- The total number of values is $N$, where $1 \le N \le 10^5$, and every value is between $1$ and $10^9$.

**Return value**

- A flat array containing every input value once in increasing `row + column` order and decreasing row order within each diagonal.

### Examples

**Example 1**

- Input: `nums = [[1,2,3],[4,5,6],[7,8,9]]`
- Output: `[1,4,2,7,5,3,8,6,9]`

**Example 2**

- Input: `nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]`
- Output: `[1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]`

**Example 3**

- Input: `nums = [[1],[2,3],[4,5,6]]`
- Output: `[1,2,4,3,5,6]`
