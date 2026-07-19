# Rank Transform of a Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1632 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Union-Find, Graph Theory, Topological Sort, Sorting, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/rank-transform-of-a-matrix/) |

## Problem Description
### Goal
Given an $R\times C$ integer matrix, assign a positive integer rank to every cell. Within any one row or column, a smaller value must have a smaller rank, an equal value must have the same rank, and a larger value must have a larger rank. Equal values that are linked through a chain of shared rows or columns must therefore be coordinated together.

Among all assignments satisfying those comparisons, every rank must be as small as possible. The test data guarantees a unique resulting matrix. Return that rank matrix without changing the input values.

### Function Contract
**Inputs**

- `matrix`: an $R\times C$ integer matrix, where $1 \le R,C \le 500$ and $-10^9 \le \texttt{matrix[r][c]} \le 10^9$.
- Let $V=RC$ be the number of cells.

**Return value**

Return an $R\times C$ matrix containing the unique minimum valid positive rank for every input cell.

### Examples
**Example 1**

- Input: `matrix = [[1,2],[3,4]]`
- Output: `[[1,2],[2,3]]`

The largest cell must exceed the rank-2 cells that precede it in its row and column.

**Example 2**

- Input: `matrix = [[7,7],[7,7]]`
- Output: `[[1,1],[1,1]]`

Every cell is connected through equal row or column values, so all receive the smallest rank.

**Example 3**

- Input: `matrix = [[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]`
- Output: `[[4,2,3],[1,3,4],[5,1,6],[1,3,4]]`
