# Check if Point Is Reachable

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2543 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [check-if-point-is-reachable](https://leetcode.com/problems/check-if-point-is-reachable/) |

## Problem Description

### Goal

Start at point `(1, 1)` on an unbounded grid. From a current point `(x, y)`, one step may produce `(x, y - x)`, `(x - y, y)`, `(2 * x, y)`, or `(x, 2 * y)`. Any finite sequence of these four operations may be used.

Given positive coordinates `targetX` and `targetY`, determine whether the target point can be reached from `(1, 1)`. Return a Boolean result.

### Function Contract

**Inputs**

- `targetX`: The positive x-coordinate of the destination.
- `targetY`: The positive y-coordinate of the destination.

Each coordinate is at most $10^9$.

**Return value**

Return `true` if some finite sequence of allowed moves reaches `(targetX, targetY)`; otherwise return `false`.

### Examples

**Example 1**

- Input: `targetX = 6, targetY = 9`
- Output: `false`
- Explanation: Their greatest common divisor is 3, which contains an odd prime factor.

**Example 2**

- Input: `targetX = 4, targetY = 7`
- Output: `true`
- Explanation: One valid route is `(1,1) -> (1,2) -> (1,4) -> (1,8) -> (1,7) -> (2,7) -> (4,7)`.
