# Score After Flipping Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 861 |
| Difficulty | Medium |
| Topics | Array, Greedy, Bit Manipulation, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/score-after-flipping-matrix/) |

## Problem Description
### Goal
You are given an $m \times n$ binary matrix `grid`. One move chooses an entire row or an entire column and toggles every value in it, changing each `0` to `1` and each `1` to `0`. Any number of moves may be made, including none.

Interpret every row from left to right as an $n$-bit binary number. The matrix score is the sum of those $m$ row values. Determine the greatest score obtainable by choosing a suitable sequence of row and column moves, and return that maximum integer.

### Function Contract
**Inputs**

- `grid`: a rectangular $m \times n$ matrix containing only `0` and `1`, where $1 \leq m,n \leq 20$.

The leftmost entry of each row is its most significant bit, with weight $2^{n-1}$; column $j$ has weight $2^{n-1-j}$.

**Return value**

Return the maximum possible sum of the binary values represented by all rows after any number of row and column toggles.

### Examples
**Example 1**

- Input: `grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]`
- Output: `39`

One optimum has rows `1111`, `1001`, and `1111`, worth $15+9+15=39$.

**Example 2**

- Input: `grid = [[0]]`
- Output: `1`

**Example 3**

- Input: `grid = [[1,1],[0,0]]`
- Output: `6`
