# Minimum Total Distance Traveled

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2463 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-total-distance-traveled/) |

## Problem Description

### Goal

Broken robots and repair factories occupy positions on the x-axis. `robot[i]` is the unique initial position of robot $i$. Each `factory[j]` is `[position, limit]`, where factory $j$ has a unique position and can repair at most `limit` robots. A robot may initially share a position with a factory.

Each robot travels continuously in one chosen direction until it reaches a factory with unused capacity, where it is repaired and stops. You may choose each robot's initial direction at any time. Robots move at equal speed, pass through one another without colliding, and pass factories whose limits are already reached. Moving from $x$ to $y$ contributes $\lvert y-x\rvert$ distance. Every robot is guaranteed to be repairable; return the minimum possible total distance traveled by all robots.

### Function Contract

**Inputs**

- `robot`: The unique integer positions of the broken robots.
- `factory`: Pairs `[position, limit]` describing unique factory positions and repair capacities.

There are at most $100$ robots and $100$ factories. Positions lie between $-10^9$ and $10^9$, each limit is between $0$ and the robot count, and total capacity is sufficient.

**Return value**

- The minimum sum of robot-to-assigned-factory distances over every capacity-respecting repair assignment.

### Examples

#### Example 1

- **Input:** `robot = [0, 4, 6], factory = [[2, 2], [6, 2]]`
- **Output:** `4`
- **Explanation:** Send the robots at `0` and `4` to position `2`, and repair the robot at `6` without movement.

#### Example 2

- **Input:** `robot = [1, -1], factory = [[-2, 1], [2, 1]]`
- **Output:** `2`
- **Explanation:** Each robot travels one unit to the factory on its respective side.
