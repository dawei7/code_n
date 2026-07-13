# Destroying Asteroids

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2126 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [destroying-asteroids](https://leetcode.com/problems/destroying-asteroids/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/destroying-asteroids/).

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

## Solution
### Approach
Sort asteroid masses in ascending order and consume them from smallest to largest. If the planet cannot destroy the smallest remaining asteroid, no other ordering can help; otherwise add that mass and continue.

### Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(1)` auxiliary space when sorting in place, excluding the sort implementation

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
