# Number of Submatrices That Sum to Target

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1074 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Matrix, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/) |

## Problem Description

### Goal

Given an integer `matrix` and an integer `target`, count the non-empty rectangular submatrices whose cell values sum exactly to `target`.

A submatrix is determined by inclusive row boundaries `x1` and `x2` and inclusive column boundaries `y1` and `y2`; it contains every `matrix[x][y]` with $x1 \le x \le x2$ and $y1 \le y \le y2$. Two submatrices are distinct whenever at least one of their four boundary coordinates differs, even if their values or sums are identical.

### Function Contract

**Inputs**

- `matrix`: an $R \times C$ integer matrix, where $1 \le R,C \le 100$ and $-1000 \le \texttt{matrix[i][j]} \le 1000$.
- `target`: an integer satisfying $-10^8 \le \texttt{target} \le 10^8$.
- Let $S=\min(R,C)$ and $L=\max(R,C)$.

**Return value**

- The number of non-empty submatrices having sum exactly `target`.

### Examples

**Example 1**

- Input: `matrix = [[0, 1, 0], [1, 1, 1], [0, 1, 0]], target = 0`
- Output: `4`
- Explanation: The four zero-valued cells are four distinct `1 x 1` submatrices.

**Example 2**

- Input: `matrix = [[1, -1], [-1, 1]], target = 0`
- Output: `5`
- Explanation: Two full rows, two full columns, and the whole matrix have sum zero.

**Example 3**

- Input: `matrix = [[904]], target = 0`
- Output: `0`
