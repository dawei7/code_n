# Find the Maximum Number of Fruits Collected

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3363 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/) |

## Problem Description

### Goal

An $n\times n$ dungeon grid stores a nonnegative fruit count in every room. Three children begin at $(0,0)$, $(0,n-1)$, and $(n-1,0)$. Each child must make exactly $n-1$ legal moves and finish at $(n-1,n-1)$. Their permitted directions differ according to their starting corner.

The first child may move right, down, or diagonally down-right. The top-right child advances one row while moving left, staying in the same column, or moving right. The bottom-left child advances one column while moving up, staying in the same row, or moving down. Entering a room collects all its fruit, but a room visited by multiple children is counted only once. Determine the maximum total fruit the three paths can collect.

### Function Contract

**Inputs**

- `fruits`: A square grid in which `fruits[i][j]` is the fruit count in room $(i,j)$.

The dimension satisfies $2\le n\le1000$, and every grid value is between $0$ and $1000$, inclusive.

**Return value**

- The maximum number of fruits collected across all three children, counting every room at most once.

### Examples

#### Example 1

- **Input:** `fruits = [[1, 2, 3, 4], [5, 6, 8, 7], [9, 10, 11, 12], [13, 14, 15, 16]]`
- **Output:** `100`
- **Explanation:** The children can use the main diagonal, a path through the strict upper triangle, and a path through the strict lower triangle, collecting ten distinct rooms.

#### Example 2

- **Input:** `fruits = [[1, 1], [1, 1]]`
- **Output:** `4`
- **Explanation:** The three starting rooms and their shared destination account for all four rooms exactly once.
