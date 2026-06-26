# Destroying Asteroids

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2126 |
| Difficulty | Medium |
| Topics | Array, Greedy, Sorting |
| Official Link | [destroying-asteroids](https://leetcode.com/problems/destroying-asteroids/) |

## Problem Description & Examples
### Goal
Decide whether a planet can destroy every asteroid. It may destroy an asteroid whose mass is no greater than its current mass, after which the asteroid's mass is added to the planet.

### Function Contract
**Inputs**

- `mass`: the planet's initial positive mass.
- `asteroids`: the positive masses of all asteroids.

**Return value**

`true` if the asteroids can be ordered so that all are destroyed; otherwise `false`.

### Examples
**Example 1**

- Input: `mass = 10`, `asteroids = [3, 9, 19, 5, 21]`
- Output: `true`

**Example 2**

- Input: `mass = 5`, `asteroids = [4, 9, 23, 4]`
- Output: `false`

**Example 3**

- Input: `mass = 1`, `asteroids = [1, 1, 2, 4]`
- Output: `true`

---

## Underlying Base Algorithm(s)
Sort asteroid masses in ascending order and consume them from smallest to largest. If the planet cannot destroy the smallest remaining asteroid, no other ordering can help; otherwise add that mass and continue.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(1)` auxiliary space when sorting in place, excluding the sort implementation
