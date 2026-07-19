# Asteroid Collision

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 735 |
| Difficulty | Medium |
| Topics | Array, Stack, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/asteroid-collision/) |

## Problem Description
### Goal
An integer array represents asteroids arranged from left to right. Each absolute value is an asteroid's size, while a positive sign means movement to the right and a negative sign means movement to the left; all asteroids move at the same speed.

Simulate every possible collision and return the surviving asteroids in left-to-right order. When opposing asteroids meet, the smaller explodes, or both explode if their sizes are equal. Asteroids moving in the same direction never collide, and two asteroids moving away from one another also cannot meet.

### Function Contract
**Inputs**

- `asteroids`: nonzero integers whose magnitudes are sizes and whose signs give direction, positive to the right and negative to the left

**Return value**

- The asteroids remaining after every possible head-on collision; the smaller asteroid disappears, and equal sizes destroy both

### Examples
**Example 1**

- Input: `asteroids = [5,10,-5]`
- Output: `[5,10]`

**Example 2**

- Input: `asteroids = [8,-8]`
- Output: `[]`

**Example 3**

- Input: `asteroids = [10,2,-5]`
- Output: `[10]`
