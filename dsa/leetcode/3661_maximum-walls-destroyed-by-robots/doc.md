# Maximum Walls Destroyed by Robots

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3661 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Dynamic Programming, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-walls-destroyed-by-robots/) |

## Problem Description
### Goal

An endless straight line contains robots and walls at integer positions. Robot `i` stands at `robots[i]` and owns one bullet whose maximum travel distance is `distance[i]`. That bullet must be fired either left or right and destroys every wall encountered within its traveled range.

Robots remain fixed and cannot be destroyed. When a bullet traveling in either direction reaches another robot, it stops there and cannot continue to any wall beyond that obstacle. A robot and a wall may occupy the same coordinate; the robot at that coordinate can destroy the wall when it fires.

Choose one firing direction for every robot to maximize the number of distinct walls destroyed. A wall struck by more than one bullet is counted only once. Return this maximum unique-wall count.

### Function Contract

**Inputs**

- `robots`: an array of $r$ distinct robot coordinates, where $1\le r\le10^5$.
- `distance`: an array of length $r$ whose value at index `i` is robot `i`'s positive range, at most $10^5$.
- `walls`: an array of $w$ distinct wall coordinates, where $1\le w\le10^5$.

Robot and wall coordinates lie between $1$ and $10^9$. The arrays need not be ordered, and each distance remains paired with the robot at the same input index.

**Return value**

Return the greatest number of unique wall coordinates that can be destroyed after every robot chooses one of its two firing directions.

### Examples

**Example 1**

- Input: `robots = [4]`, `distance = [3]`, `walls = [1, 10]`
- Output: `1`
- Firing left reaches the wall at `1`; firing right reaches neither wall.

**Example 2**

- Input: `robots = [10, 2]`, `distance = [5, 1]`, `walls = [5, 2, 7]`
- Output: `3`
- The robot at `10` fires left through `7` and `5`, while the robot at `2` destroys its co-located wall.

**Example 3**

- Input: `robots = [1, 2]`, `distance = [100, 1]`, `walls = [10]`
- Output: `0`
- The robot at `2` blocks the first robot's rightward bullet before it can reach `10`.
