# Minimum Health to Beat Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2214 |
| Difficulty | Medium |
| Topics | Array, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-health-to-beat-game/) |

## Problem Description
### Goal

You must complete a sequence of game levels in their given order. Level $i$ reduces your health by `damage[i]`. Your health must remain strictly greater than zero throughout the game; reaching zero is not enough to survive.

You also have armor that may be used on at most one level. On that level it prevents up to `armor` points of damage, but it cannot prevent more damage than the level deals. Determine the minimum health with which you can start and still finish every level.

### Function Contract
**Inputs**

- `damage`: A nonempty list where `damage[i]` is the nonnegative health loss caused by level $i$.
- `armor`: A nonnegative integer giving the maximum damage the one-use armor can prevent.

Let $n$ be the number of levels.

**Return value**

Return the minimum positive integer starting health that lets you complete all $n$ levels while using the armor at most once.

### Examples
**Example 1**

- Input: `damage = [2, 7, 4, 3], armor = 4`
- Output: `13`

**Example 2**

- Input: `damage = [2, 5, 3, 4], armor = 7`
- Output: `10`

**Example 3**

- Input: `damage = [3, 3, 3], armor = 0`
- Output: `10`
