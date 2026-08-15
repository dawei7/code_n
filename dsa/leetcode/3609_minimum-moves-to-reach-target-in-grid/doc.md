# Minimum Moves to Reach Target in Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3609 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-moves-to-reach-target-in-grid/) |

## Problem Description

### Goal

Two points `(sx, sy)` and `(tx, ty)` lie on an infinitely large two-dimensional grid. Start at `(sx, sy)`. At a current point $(x,y)$, let $m = \max(x,y)$. One move may add $m$ to exactly one coordinate, changing the point to either $(x+m,y)$ or $(x,y+m)$.

Find the minimum number of moves needed to reach `(tx, ty)`. Return `-1` when no sequence of allowed moves reaches the target. The starting coordinates do not exceed their corresponding target coordinates, and all coordinates are nonnegative.

### Function Contract

**Inputs**

- `sx`: The starting x-coordinate.
- `sy`: The starting y-coordinate.
- `tx`: The target x-coordinate.
- `ty`: The target y-coordinate.

The constraints are $0 \le \texttt{sx} \le \texttt{tx} \le 10^9$ and $0 \le \texttt{sy} \le \texttt{ty} \le 10^9$.

**Return value**

Return the minimum number of legal moves from the start to the target, or `-1` if the target is unreachable.

### Examples

#### Example 1

- **Input:** `sx = 1, sy = 2, tx = 5, ty = 4`
- **Output:** `2`
- **Explanation:** Move from `(1, 2)` to `(1, 4)`, then to `(5, 4)`.

#### Example 2

- **Input:** `sx = 0, sy = 1, tx = 2, ty = 3`
- **Output:** `3`
- **Explanation:** A shortest route is `(0, 1)`, `(1, 1)`, `(2, 1)`, `(2, 3)`.

#### Example 3

- **Input:** `sx = 1, sy = 1, tx = 2, ty = 2`
- **Output:** `-1`
- **Explanation:** Neither legal first move can lead to `(2, 2)`.
