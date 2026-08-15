# Median of a Row Wise Sorted Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2387 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/median-of-a-row-wise-sorted-matrix/) |

## Problem Description

### Goal

Given an $m \times n$ integer matrix `grid`, treat all of its entries as one collection and return its median. Both dimensions are odd, so the matrix contains an odd number of values and the median is the single middle value after global ordering.

Each row is independently sorted in non-decreasing order, but values in different rows have no ordering relationship. The solution must exploit that row structure and run in strictly less than $O(mn)$ time rather than reading and sorting every entry.

### Function Contract

**Inputs**

- `grid`: An $m \times n$ matrix, where $1 \le m,n \le 500$, both dimensions are odd, and every row is sorted in non-decreasing order.

Every entry lies between 1 and $10^6$ inclusive.

**Return value**

- Return the value at global sorted rank $(mn+1)/2$.

**Median semantics**

- Repeated values occupy separate ranks.
- Only rows are sorted; columns need not be ordered.
- The required running time is strictly below $O(mn)$.

### Examples

#### Example 1

- **Input:** `grid = [[1,1,2],[2,3,3],[1,3,4]]`
- **Output:** `2`

#### Example 2

- **Input:** `grid = [[1,1,3,3,4]]`
- **Output:** `3`
