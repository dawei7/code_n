# Unique Paths III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 980 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Backtracking, Bit Manipulation, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/unique-paths-iii/) |

## Problem Description

### Goal

An $M\times N$ integer grid contains exactly one starting square marked `1` and exactly one ending square marked `2`. Empty squares marked `0` may be walked over, while obstacles marked `-1` cannot be entered.

Count the four-directional walks from the starting square to the ending square that visit every non-obstacle square exactly once. Each step moves up, down, left, or right to an edge-adjacent square; diagonal movement is not allowed. A walk is valid only if it reaches the ending square after covering the start, every empty square, and the end itself without revisiting any of them.

### Function Contract

**Inputs**

- `grid`: an $M\times N$ integer matrix with $1\le M,N\le20$, $1\le MN\le20$, values from `-1` through `2`, and exactly one start and one end.

Let $V$ be the number of non-obstacle squares.

**Return value**

- The number of four-directional start-to-end walks that visit all $V$ usable squares exactly once.

### Examples

**Example 1**

- Input: `grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]`
- Output: `2`

**Example 2**

- Input: `grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]`
- Output: `4`

**Example 3**

- Input: `grid = [[0, 1], [2, 0]]`
- Output: `0`
- Explanation: no walk covers both empty squares exactly once before ending.
