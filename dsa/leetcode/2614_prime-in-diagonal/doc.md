# Prime In Diagonal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2614 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math, Matrix, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/prime-in-diagonal/) |

## Problem Description

### Goal

You are given a 0-indexed square integer matrix `nums`. A value lies on a diagonal when it occurs either at `nums[i][i]` on the primary diagonal or at `nums[i][n - 1 - i]` on the secondary diagonal for some row index $i$.

Find the largest prime number appearing on at least one of these two diagonals. A prime is an integer greater than $1$ whose only positive divisors are $1$ and itself. Return $0$ when neither diagonal contains a prime.

### Function Contract

**Inputs**

Let $n$ be the side length of the matrix.

- `nums`: An $n \times n$ integer matrix, where $1 \leq n \leq 300$ and $1 \leq \texttt{nums}[i][j] \leq 4\cdot 10^6$.

**Return value**

Return the largest prime value found on the primary or secondary diagonal. Return $0$ if every value on both diagonals is non-prime.

### Examples

**Example 1**

- Input: `nums = [[1, 2, 3], [5, 6, 7], [9, 10, 11]]`
- Output: `11`
- Explanation: The diagonal values are $1,3,6,9,11$; the largest prime among them is $11$.

**Example 2**

- Input: `nums = [[1, 2, 3], [5, 17, 7], [9, 11, 10]]`
- Output: `17`
- Explanation: The center value belongs to both diagonals, and $17$ is the largest diagonal prime.

**Example 3**

- Input: `nums = [[4, 4], [4, 4]]`
- Output: `0`
- Explanation: Neither diagonal contains a prime number.
