# Transform to Chessboard

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 782 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Bit Manipulation, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/transform-to-chessboard/) |

## Problem Description

### Goal

Given an $n \times n$ binary matrix `board`, one move may swap any two complete rows or any two complete columns. A chessboard is an arrangement in which every pair of horizontally or vertically adjacent cells contains different values.

Return the minimum number of row and column swaps needed to transform `board` into a chessboard. If no sequence of allowed whole-row and whole-column swaps can produce one, return `-1`. Individual cells cannot be swapped independently, and diagonal equality does not violate the chessboard condition.

### Function Contract

**Inputs**

- `board`: a nonempty $n \times n$ matrix containing only `0` and `1`.

**Return value**

- The minimum number of row and column swaps that transforms `board` into a chessboard, or `-1` if transformation is impossible.

### Examples

**Example 1**

- Input: `board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]`
- Output: `2`
- Explanation: One row swap and one column swap create alternating rows and columns.

**Example 2**

- Input: `board = [[0,1],[1,0]]`
- Output: `0`
- Explanation: The board already has chessboard adjacency.

**Example 3**

- Input: `board = [[1,0],[1,0]]`
- Output: `-1`
- Explanation: Swapping whole rows or columns cannot make the two rows complementary.
