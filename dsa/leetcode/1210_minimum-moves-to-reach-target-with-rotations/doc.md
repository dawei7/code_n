# Minimum Moves to Reach Target with Rotations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1210 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Breadth-First Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/) |

## Problem Description

### Goal

An $n\times n$ grid contains empty cells marked `0` and blocked cells marked `1`. A snake spans two adjacent cells. It begins horizontally across `(0, 0)` and `(0, 1)` and must finish horizontally across `(n - 1, n - 2)` and `(n - 1, n - 1)`.

In one move, the snake may translate one cell right or one cell down while preserving its orientation, provided both destination cells are empty. A horizontal snake at `(r, c)` and `(r, c + 1)` may rotate clockwise around `(r, c)` when both cells directly below it are empty, becoming vertical at `(r, c)` and `(r + 1, c)`. A vertical snake at `(r, c)` and `(r + 1, c)` may rotate counterclockwise around `(r, c)` when both cells directly to its right are empty, becoming horizontal at `(r, c)` and `(r, c + 1)`.

Return the minimum number of moves needed to reach the target. If no valid sequence reaches it, return `-1`.

### Function Contract

**Inputs**

- `grid`: An $n\times n$ binary matrix, where $2\le n\le100$; zero cells are empty and one cells are blocked.
- The two starting cells are guaranteed to be empty.

**Return value**

- The fewest translations and rotations required to reach the bottom-right horizontal target, or `-1` when it is unreachable.

### Examples

**Example 1**

- Input: `grid = [[0,0,0,0,0,1],[1,1,0,0,1,0],[0,0,0,0,1,1],[0,0,1,0,1,0],[0,1,1,0,0,0],[0,1,1,0,0,0]]`
- Output: `11`

One shortest sequence uses translations in both directions and both allowed rotations.

**Example 2**

- Input: `grid = [[0,0,1,1,1,1],[0,0,0,0,1,1],[1,1,0,0,0,1],[1,1,1,0,0,1],[1,1,1,0,0,1],[1,1,1,0,0,0]]`
- Output: `9`

**Example 3**

- Input: `grid = [[0,0],[0,0]]`
- Output: `1`
