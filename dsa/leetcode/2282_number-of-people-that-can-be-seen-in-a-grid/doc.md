# Number of People That Can Be Seen in a Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2282 |
| Difficulty | Medium |
| Topics | Array, Stack, Matrix, Monotonic Stack |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-people-that-can-be-seen-in-a-grid/) |

## Problem Description
### Goal
An $m \times n$ grid contains one person in each cell, and
`heights[i][j]` gives that person's positive height. A person may look only
to the right within the same row or downward within the same column.

The person in one cell can see a later person in one of those directions
exactly when every person strictly between them is shorter than both endpoint
people. Return an $m \times n$ matrix whose entry at `(i, j)` counts everyone
visible to the right or below the person in that cell.

### Function Contract
**Inputs**

- `heights`: A rectangular $m \times n$ integer matrix containing the height of each person.

Here, $1 \le m,n \le 400$ and
$1 \le \texttt{heights[i][j]} \le 10^5$.

**Return value**

An $m \times n$ integer matrix where each entry is the number of people visible
from the corresponding input cell in the two permitted directions.

### Examples
**Example 1**

- Input: `heights = [[3, 1, 4, 2, 5]]`
- Output: `[[2, 1, 2, 1, 0]]`

**Example 2**

- Input: `heights = [[5, 1], [3, 1], [4, 1]]`
- Output: `[[3, 1], [2, 1], [1, 0]]`

**Example 3**

- Input: `heights = [[2, 2], [2, 2]]`
- Output: `[[2, 1], [1, 0]]`
