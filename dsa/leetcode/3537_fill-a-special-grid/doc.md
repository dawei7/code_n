# Fill a Special Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3537 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Divide and Conquer, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/fill-a-special-grid/) |

## Problem Description

### Goal

For a non-negative integer `n`, construct a square grid with side length $2^n$. Fill its $2^{2n}$ cells with every integer from $0$ through $2^{2n}-1$ exactly once.

A grid larger than one cell is special when its four equal quadrants obey this strict value order: every value in the top-right quadrant is smaller than every value in the bottom-right quadrant; every bottom-right value is smaller than every bottom-left value; and every bottom-left value is smaller than every top-left value. Each quadrant must itself be special under the same recursive definition.

Any $1\times1$ grid is special. Return the resulting special grid.

### Function Contract

**Inputs**

- `n`: The grid exponent, where $0 \le n \le 10$.

The grid has side length $2^n$ and contains $4^n$ cells. Let $k=4$ denote the fixed number of recursive quadrants, so this output size is also $k^n$.

**Return value**

- A $2^n\times2^n$ integer matrix satisfying the recursive quadrant ordering and containing every value in $[0,4^n-1]$ once.

### Examples

**Example 1**

- Input: `n = 0`
- Output: `[[0]]`
- Explanation: The one-cell base case contains the only available value.

**Example 2**

- Input: `n = 1`
- Output: `[[3,0],[2,1]]`
- Explanation: The one-cell quadrants appear in increasing order from top-right to bottom-right to bottom-left to top-left.

**Example 3**

- Input: `n = 2`
- Output: `[[15,12,3,0],[14,13,2,1],[11,8,7,4],[10,9,6,5]]`
- Explanation: Each quadrant repeats the same special pattern, with successive value blocks assigned in the required quadrant order.
