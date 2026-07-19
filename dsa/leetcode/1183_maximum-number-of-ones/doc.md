# Maximum Number of Ones

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1183 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, Greedy, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-ones/) |

## Problem Description

### Goal

Consider a binary matrix `M` with `height` rows and `width` columns. Every cell is either `0` or `1`. Its entries may be chosen freely, except that every contiguous square submatrix with dimensions `sideLength * sideLength` must contain at most `maxOnes` cells whose value is `1`.

Determine the maximum possible number of ones in the entire matrix while satisfying that restriction simultaneously for every such square. Only the maximum count is required; the matrix itself does not need to be returned.

### Function Contract

**Inputs**

- `width`: The number of matrix columns, with $1\le\texttt{width}\le100$.
- `height`: The number of matrix rows, with $1\le\texttt{height}\le100$.
- `sideLength`: The side length $s$ of every constrained square, where $1\le s\le\min(\texttt{width},\texttt{height})$.
- `maxOnes`: The inclusive limit on ones in each constrained square, where $0\le\texttt{maxOnes}\le s^2$.

**Return value**

- The greatest total number of `1` cells achievable in the full `height * width` matrix without any `sideLength * sideLength` submatrix exceeding `maxOnes` ones.

### Examples

**Example 1**

- Input: `width = 3`, `height = 3`, `sideLength = 2`, `maxOnes = 1`
- Output: `4`

One optimal matrix places ones at its four corners. Every `2 * 2` submatrix then contains exactly one of them.

**Example 2**

- Input: `width = 3`, `height = 3`, `sideLength = 2`, `maxOnes = 2`
- Output: `6`

For example, the first and third columns can be filled with ones while the middle column remains zero.
