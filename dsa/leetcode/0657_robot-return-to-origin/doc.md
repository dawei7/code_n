# Robot Return to Origin

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 657 |
| Difficulty | Easy |
| Topics | String, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/robot-return-to-origin/) |

## Problem Description
### Goal
A robot starts at `(0, 0)`, the origin of a two-dimensional plane. The string `moves` gives its sequence of unit movements: `R` moves right, `L` left, `U` up, and `D` down.

Return `True` if the robot is back at `(0, 0)` after completing every move, and `False` otherwise. The robot's facing direction is irrelevant: each character always moves in its named absolute direction, and every move has the same magnitude. Visiting the origin before the sequence ends is insufficient unless the final position is also the origin.

### Function Contract
**Inputs**

- `moves`: a nonempty string containing only `U`, `D`, `L`, and `R`

**Return value**

- `True` when the final position is the origin; otherwise `False`

### Examples
**Example 1**

- Input: `moves = "UD"`
- Output: `True`

**Example 2**

- Input: `moves = "LL"`
- Output: `False`

**Example 3**

- Input: `moves = "URDL"`
- Output: `True`
