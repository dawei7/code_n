# Maximum Profit of Operating a Centennial Wheel

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1599 |
| Difficulty | Medium |
| Topics | Array, Simulation |
| Official Link | [maximum-profit-of-operating-a-centennial-wheel](https://leetcode.com/problems/maximum-profit-of-operating-a-centennial-wheel/) |

## Problem Description & Examples
### Goal
Simulate a wheel that boards up to four waiting customers per rotation and find
the rotation count that gives the highest profit.

### Function Contract
**Inputs**

- `customers`: arrivals before each rotation.
- `boardingCost`: revenue per boarded customer.
- `runningCost`: cost per rotation.

**Return value**

The earliest rotation with maximum positive profit, or `-1` if operating never
becomes profitable.

### Examples
**Example 1**

- Input: `customers = [8, 3], boardingCost = 5, runningCost = 6`
- Output: `3`

**Example 2**

- Input: `customers = [10, 9, 6], boardingCost = 6, runningCost = 4`
- Output: `7`

**Example 3**

- Input: `customers = [3, 4, 0, 5, 1], boardingCost = 1, runningCost = 92`
- Output: `-1`

---

## Underlying Base Algorithm(s)
Simulate rotations while there are unprocessed arrivals or waiting customers.
Add new arrivals, board `min(4, waiting)` customers, update profit, and record
the earliest rotation where profit is strictly greater than the best seen so
far.

---

## Complexity Analysis
- **Time Complexity**: `O(n + extra)`, where `extra` is the number of rotations needed to clear the queue.
- **Space Complexity**: `O(1)`.
