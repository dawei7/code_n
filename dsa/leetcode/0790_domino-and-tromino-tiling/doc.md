# Domino and Tromino Tiling

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 790 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/domino-and-tromino-tiling/) |

## Problem Description

### Goal

Given a $2 x n$ board, tile every cell using $2 x 1$ dominoes and trominoes formed from three cells in an L shape. Either tile type may be rotated into any orientation that fits the board.

Return the number of complete tilings modulo `1,000,000,007`. Tiles may not overlap or extend outside the board, and every board cell must be covered exactly once. Two tilings are different when any domino or tromino occupies a different set of cells.

### Function Contract

**Inputs**

- `n`: the positive width of the two-row board.

**Return value**

- The number of complete tilings modulo `1,000,000,007`.

### Examples

**Example 1**

- Input: `n = 1`
- Output: `1`
- Explanation: One vertical domino covers the board.

**Example 2**

- Input: `n = 2`
- Output: `2`
- Explanation: Use two vertical dominoes or two horizontal dominoes.

**Example 3**

- Input: `n = 3`
- Output: `5`
- Explanation: Three domino-only arrangements and two arrangements using a pair of trominoes are possible.
