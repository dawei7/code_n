# Robot Room Cleaner

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 489 |
| Difficulty | Hard |
| Topics | Backtracking, Interactive |
| Official Link | [LeetCode](https://leetcode.com/problems/robot-room-cleaner/) |

## Problem Description
### Goal
Control a robot placed in an unknown room whose walls, dimensions, starting coordinates, and starting orientation are hidden. The interface only lets the robot attempt to move one cell forward, turn left or right by 90 degrees, and clean its current cell; a blocked move leaves it in place and reports failure.

Use those local operations to clean every open cell reachable from the starting position, without entering blocked cells or requiring access to the underlying grid. The robot may revisit cells while exploring, but it must restore enough position and orientation state to reach unexplored branches. No return value is required; completion is measured by the set of reachable cells cleaned.

### Function Contract
**Inputs**

- `robot`: an interface exposing `move()`, `turnLeft()`, `turnRight()`, and `clean()`

**Return value**

- `None`; success is the side effect of cleaning every reachable cell

### Examples
**Example 1**

- Input: `robot = a robot alone in one open cell`
- Output: `None`

**Example 2**

- Input: `robot = a robot inside a four-cell corridor`
- Output: `None`

**Example 3**

- Input: `robot = a robot in an eight-cell ring around an obstacle`
- Output: `None`
