# Car Fleet II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1776 |
| Difficulty | Hard |
| Topics | Array, Math, Stack, Heap (Priority Queue), Monotonic Stack |
| Official Link | [car-fleet-ii](https://leetcode.com/problems/car-fleet-ii/) |

## Problem Description & Examples
### Goal
Cars travel along a one-lane road in increasing position order. When a faster car catches the next car or fleet ahead, they merge and move at the slower speed. For each car, find when it first collides with another car or fleet.

### Function Contract
**Inputs**

- `cars`: a list of `[position, speed]` pairs sorted by position.

**Return value**

Return an array of collision times, using `-1` for cars that never collide.

### Examples
**Example 1**

- Input: `cars = [[1,2],[2,1],[4,3],[7,2]]`
- Output: `[1.00000,-1.00000,3.00000,-1.00000]`

**Example 2**

- Input: `cars = [[3,4],[5,4],[6,3],[9,1]]`
- Output: `[2.00000,1.00000,1.50000,-1.00000]`

**Example 3**

- Input: `cars = [[1,1],[2,2],[3,3]]`
- Output: `[-1.00000,-1.00000,-1.00000]`

---

## Underlying Base Algorithm(s)
Process cars from right to left with a monotonic stack of candidate cars/fleets ahead. A car can only collide with a slower candidate. Pop candidates that are not slower, or that would have already collided before this car reaches them. The next remaining candidate gives the collision time.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`
