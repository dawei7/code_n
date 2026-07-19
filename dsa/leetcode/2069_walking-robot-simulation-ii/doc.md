# Walking Robot Simulation II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2069 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Design, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/walking-robot-simulation-ii/) |

## Problem Description

### Goal

A `width` by `height` grid lies on an XY-plane, from `(0,0)` at the bottom-left through `(width - 1, height - 1)` at the top-right. A robot begins at `(0,0)` facing `East`.

For each requested step, the robot tries to move one cell forward. If that cell would be outside the grid, it first turns $90^\circ$ counterclockwise and retries the same step. After completing an instruction, its position and current direction persist for later calls.

Implement the stateful `Robot` class. It must accept movement instructions and report the current position or one of `East`, `North`, `West`, and `South` as the direction.

### Function Contract

**Inputs**

- `Robot(width, height)`: initialize a grid with $2 \le \texttt{width},\texttt{height}\le100$.
- `step(num)`: move the robot by exactly `num` successful cell steps, where $1 \le \texttt{num}\le10^5$.
- `getPos()`: request the current `[x,y]` position.
- `getDir()`: request the current cardinal direction.

At most $Q=10^4$ method calls are made after construction.

**Return value**

- `step` returns no value.
- `getPos` returns `[x,y]`.
- `getDir` returns the current direction string.
- In the app adapter, return the result of every operation in order, using `null` for construction and `step`.

### Examples

**Example 1**

- Input: `operations = ["Robot","step","step","getPos","getDir","step","step","step","getPos","getDir"]`, `arguments = [[6,3],[2],[2],[],[],[2],[1],[4],[],[]]`
- Output: `[null,null,null,[4,0],"East",null,null,null,[1,2],"West"]`
- Explanation: The robot crosses the bottom edge, turns north at the right boundary, and later turns west across the top edge.
