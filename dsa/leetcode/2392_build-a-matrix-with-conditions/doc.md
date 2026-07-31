# Build a Matrix With Conditions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2392 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Graph Theory, Topological Sort, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/build-a-matrix-with-conditions/) |

## Problem Description

### Goal

Given an integer `k`, construct a $k \times k$ matrix containing each value from 1 through `k` exactly once; every other cell must be zero. Two collections impose independent precedence requirements on the rows and columns.

For every pair `[above, below]` in `rowConditions`, `above` must occupy a strictly smaller row index than `below`. For every `[left, right]` in `colConditions`, `left` must occupy a strictly smaller column index than `right`. Return any matrix satisfying all conditions. If either collection is contradictory, return an empty matrix.

### Function Contract

**Inputs**

- `k`: The number of rows, columns, and nonzero values, where $2 \le k \le 400$.
- `rowConditions`: Between 1 and $10^4$ directed row constraints.
- `colConditions`: Between 1 and $10^4$ directed column constraints.

Every endpoint lies from 1 through `k`, and the endpoints of one condition differ.

Let $r$ and $c$ denote the numbers of row and column conditions.

**Return value**

- Return any valid $k \times k$ matrix, or `[]` when no valid placement exists.

**Placement semantics**

- Every value from 1 through `k` appears exactly once.
- Zeros fill all other cells.
- Row and column constraints are independent and may each admit many orders.

### Examples

**Example 1**

- Input: `k = 3, rowConditions = [[1,2],[3,2]], colConditions = [[2,1],[3,2]]`
- One valid output: `[[3,0,0],[0,0,1],[0,2,0]]`

**Example 2**

- Input: `k = 3, rowConditions = [[1,2],[2,3],[3,1],[2,3]], colConditions = [[2,1]]`
- Output: `[]`
- Explanation: The row conditions contain a directed cycle.
