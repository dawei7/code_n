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

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

Each column sum fixes how its two bits can look. A zero forces `[0, 0]`, a two forces `[1, 1]`, and a one must place exactly one bit in either row. This makes the columns with sum two mandatory and leaves only the sum-one columns to distribute.

**Commit the forced columns first**

For every `colsum[i] == 2`, set both output entries to `1` and decrement both remaining row sums. If either remaining requirement becomes negative, the forced ones already exceed that row's target, so no reconstruction exists.

**Distribute flexible columns greedily**

For a column with sum one, assign its single `1` to a row that still needs one. Choosing the row with the larger remaining requirement keeps the demands balanced, although assigning to either positive remainder is sufficient. Decrement the selected remainder after the assignment.

After all columns, both remainders must be zero. If so, every column has its required sum and both row totals match. If either remainder is nonzero, there were not enough sum-one columns to meet the requested totals, so return `[]`.

#### Complexity detail

The two passes inspect the $n$ columns a constant number of times, taking $O(n)$ time. The two output rows contain $2n$ bits and therefore require $O(n)$ space; auxiliary counters use $O(1)$ space beyond the returned matrix.

#### Alternatives and edge cases

- **Backtracking over sum-one columns:** It explores every distribution and can take exponential time even though only the remaining row totals matter.
- **Count-only feasibility check:** Counting sum-two and sum-one columns can decide existence, but a second step is still needed to construct the requested matrix.
- **Too many forced ones:** If the number of sum-two columns exceeds either row target, return `[]` immediately.
- **Mismatched total:** A necessary condition is $\texttt{upper}+\texttt{lower}=\sum_i \texttt{colsum[i]}$; the final remainder check enforces it.
- **Zero row target:** Every flexible one must go to the other row, while any sum-two column makes a zero target impossible.
- **Multiple answers:** The order in which flexible columns are assigned may change the matrix without affecting validity.

</details>
