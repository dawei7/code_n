# The Knight's Tour

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2664 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Backtracking, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/the-knights-tour/) |

## Problem Description

### Goal

You are given the positive dimensions `m` and `n` of a 0-indexed rectangular board, together with the knight's starting cell `(r, c)`. Construct a sequence of legal chess-knight moves that visits every board cell exactly once. The starting cell counts as the first visit and must not be visited again.

A move from `(r1, c1)` to `(r2, c2)` is legal when the destination remains inside the board and the absolute row and column differences are $1$ and $2$ in either order. Equivalently,

$$
\min(\lvert r_1-r_2 \rvert,\lvert c_1-c_2 \rvert)=1
\quad\text{and}\quad
\max(\lvert r_1-r_2 \rvert,\lvert c_1-c_2 \rvert)=2.
$$

Return an `m` by `n` matrix whose value at each cell is its visit index, beginning with `0` at `(r, c)` and ending with `m * n - 1`. The input guarantee ensures that at least one complete tour exists. More than one output can therefore be valid.

### Function Contract

**Inputs**

- `m`: The number of board rows, where $1 \le m \le 5$.
- `n`: The number of board columns, where $1 \le n \le 5$.
- `r`: The starting row, where $0 \le r < m$.
- `c`: The starting column, where $0 \le c < n$.

Only dimension and start combinations admitting at least one full tour are supplied.

**Return value**

- Return an `m` by `n` integer matrix encoding one legal complete tour with visit numbers from `0` through `m * n - 1`.

### Examples

**Example 1**

- Input: `m = 1, n = 1, r = 0, c = 0`
- Output: `[[0]]`
- Explanation: The starting cell is the entire board, so the tour is already complete.

**Example 2**

- Input: `m = 3, n = 4, r = 0, c = 0`
- Output: `[[0,3,6,9],[11,8,1,4],[2,5,10,7]]`
- Explanation: Reading cells in visit-number order gives a legal knight move at every step. Other complete tours are also accepted.
