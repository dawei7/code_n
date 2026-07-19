# Largest Submatrix With Rearrangements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1727 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/largest-submatrix-with-rearrangements/) |

## Problem Description

### Goal

You are given an $m\times n$ binary matrix. You may rearrange its columns in any order: moving a column moves that entire column, so the relative vertical contents of every column remain unchanged. After choosing the column order, consider ordinary rectangular submatrices of the rearranged matrix.

Return the largest possible area of a submatrix in which every element is `1`. The column order may be chosen specifically to maximize this one rectangle, but entries within a column and the order of the rows cannot be changed.

### Function Contract

**Inputs**

- `matrix`: an $m\times n$ array whose entries are `0` or `1`, where $1 \le mn \le 10^5$.

**Return value**

- Return the maximum area of an all-ones rectangular submatrix obtainable after one optimal rearrangement of the complete columns.

### Examples

**Example 1**

- Input: `matrix = [[0,0,1],[1,1,1],[1,0,1]]`
- Output: `4`
- Explanation: Reordering complete columns can place two columns with height-two runs next to each other, producing an all-ones rectangle of height two and width two.

**Example 2**

- Input: `matrix = [[1,0,1,0,1]]`
- Output: `3`
- Explanation: Place the three columns containing `1` together to form a one-row rectangle of width three.

**Example 3**

- Input: `matrix = [[1,1,0],[1,0,1]]`
- Output: `2`
- Explanation: Entire columns must move together; the rows cannot select independent column orders.
