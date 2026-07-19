# Reconstruct a 2-Row Binary Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1253 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/) |

## Problem Description

### Goal

Construct a binary matrix with exactly two rows and $n$ columns. The sum of the first row must equal `upper`, the sum of the second row must equal `lower`, and the sum of the two entries in column `i` must equal `colsum[i]`.

Return any matrix satisfying all three requirements. Every entry must be either `0` or `1`. If no such two-row matrix exists, return an empty list. Different valid distributions for columns whose required sum is `1` are equally acceptable.

### Function Contract

**Inputs**

- `upper`: the required first-row sum, with $0 \le \texttt{upper} \le n$.
- `lower`: the required second-row sum, with $0 \le \texttt{lower} \le n$.
- `colsum`: an array of length $n$, where $1 \le n \le 10^5$ and every value is `0`, `1`, or `2`.

**Return value**

- Return any valid `2 x n` binary matrix, or `[]` when reconstruction is impossible.

### Examples

**Example 1**

- Input: `upper = 2`, `lower = 1`, `colsum = [1, 1, 1]`
- Output: `[[1, 1, 0], [0, 0, 1]]`

**Example 2**

- Input: `upper = 2`, `lower = 3`, `colsum = [2, 2, 1, 1]`
- Output: `[]`

**Example 3**

- Input: `upper = 5`, `lower = 5`, `colsum = [2, 1, 2, 0, 1, 0, 1, 2, 0, 1]`
- Output: one valid matrix is `[[1, 1, 1, 0, 1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 0, 0, 1, 1, 0, 1]]`.
