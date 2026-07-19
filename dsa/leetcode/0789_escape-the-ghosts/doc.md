# Escape The Ghosts

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 789 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/escape-the-ghosts/) |

## Problem Description

### Goal

You start at `(0, 0)` on an unbounded integer grid, while each ghost starts at its supplied coordinate. During every turn, you and every ghost may move one unit horizontally or vertically, and all participants may choose their routes.

Return `True` if you can guarantee reaching `target` before every ghost can intercept you there or along the way, and `False` otherwise. A ghost reaching your position at the same time is enough to prevent escape, and ghosts choose their movements adversarially rather than randomly.

### Function Contract

**Inputs**

- `ghosts`: a list of starting coordinates `[x, y]` for the ghosts.
- `target`: the destination coordinate `[x, y]`.

**Return value**

- `True` if you can guarantee reaching the target before every ghost; otherwise `False`.

### Examples

**Example 1**

- Input: `ghosts = [[1,0],[0,3]], target = [0,1]`
- Output: `True`
- Explanation: You need one move, while each ghost needs at least two moves to reach the target.

**Example 2**

- Input: `ghosts = [[1,0]], target = [2,0]`
- Output: `False`
- Explanation: The ghost can reach the target in one move, before your two-move route finishes.

**Example 3**

- Input: `ghosts = [[2,0]], target = [1,0]`
- Output: `False`
- Explanation: Both you and the ghost can arrive after one move, and a tie is not an escape.
