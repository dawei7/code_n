# Spiral Matrix IV

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2326 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Linked List, Matrix, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/spiral-matrix-iv/) |

## Problem Description

### Goal

Create a matrix with `m` rows and `n` columns, then consume the values of the
given singly linked list in their existing order. Place the first value in the
top-left cell and continue clockwise across the top row, down the right side,
back across the bottom, and up the left side.

Continue the same clockwise spiral through successive inner layers until the
linked list has no nodes left. The list contains at most $mn$ nodes, so it
never exceeds the matrix capacity. Every cell that receives no list value must
contain `-1`; return the complete matrix.

### Function Contract

**Inputs**

- `m`: The number of rows, with $1 \le m \le 10^5$.
- `n`: The number of columns, with $1 \le n \le 10^5$ and
  $1 \le mn \le 10^5$.
- `head`: The head of a singly linked list containing between 1 and $mn$
  nodes. Every node value lies in $[0,1000]$.

**Return value**

An `m` by `n` integer matrix containing list values in clockwise spiral order
from the top-left, with every unused cell set to `-1`.

### Examples

**Example 1**

- Input: `m = 3`, `n = 5`,
  `head = [3,0,2,6,8,1,7,9,4,2,5,5,0]`
- Output: `[[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]`
- Explanation: Thirteen values occupy the outer spiral and part of the inner
  row; the two cells never reached remain `-1`.

**Example 2**

- Input: `m = 1`, `n = 4`, `head = [0,1,2]`
- Output: `[[0,1,2,-1]]`
- Explanation: A one-row spiral moves only from left to right.

**Example 3**

- Input: `m = 2`, `n = 2`, `head = [1000,0,500,250]`
- Output: `[[1000,0],[250,500]]`
- Explanation: A full two-by-two perimeter visits the bottom-right cell before
  the bottom-left cell.
