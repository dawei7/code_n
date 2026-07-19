# Moving Stones Until Consecutive

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1033 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Brainteaser |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/moving-stones-until-consecutive/) |

## Problem Description

### Goal

Three stones occupy different integer positions `a`, `b`, and `c` on the x-axis.

In one move, sort the current positions as `x < y < z`, pick up an endpoint stone at `x` or `z`, and place it at an unoccupied integer position `k` satisfying `x < k < z` and `k != y`. The game ends when no move is possible, which occurs when the stones occupy three consecutive positions.

Return `[minimum_moves, maximum_moves]`, where the two values are respectively the fewest and greatest numbers of legal moves that can be played before the game ends.

### Function Contract

**Inputs**

- `a`, `b`, and `c`: three distinct stone positions, each between $1$ and $100$, inclusive.

**Return value**

- A two-element array containing the minimum and maximum possible move counts.

### Examples

**Example 1**

- Input: `a = 1, b = 2, c = 5`
- Output: `[1,2]`
- Explanation: Move `5` directly to `3` for the minimum, or move it first to `4` and then to `3` for the maximum.

**Example 2**

- Input: `a = 4, b = 3, c = 2`
- Output: `[0,0]`
- Explanation: The sorted positions are already consecutive.

**Example 3**

- Input: `a = 3, b = 5, c = 1`
- Output: `[1,2]`
- Explanation: Move `1` directly to `4`, or move it through `2` before reaching `4`.
