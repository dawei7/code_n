# Minimum Speed to Arrive on Time

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1870 |
| Difficulty | Medium |
| Topics | Array, Binary Search |
| Official Link | [minimum-speed-to-arrive-on-time](https://leetcode.com/problems/minimum-speed-to-arrive-on-time/) |

## Problem Description & Examples
### Goal
Trains travel several distances at one chosen integer speed. All but the last train departure must wait until the next integer hour. Find the minimum speed that arrives within the given time.

### Function Contract
**Inputs**

- `dist`: distances of the train rides.
- `hour`: maximum allowed total travel time.

**Return value**

Return the minimum integer speed, or `-1` if arriving on time is impossible.

### Examples
**Example 1**

- Input: `dist = [1,3,2], hour = 6`
- Output: `1`

**Example 2**

- Input: `dist = [1,3,2], hour = 2.7`
- Output: `3`

**Example 3**

- Input: `dist = [1,3,2], hour = 1.9`
- Output: `-1`

---

## Underlying Base Algorithm(s)
Binary search the speed. For a candidate speed, compute total time as the sum of `ceil(dist[i] / speed)` for every ride except the last, plus exact last ride time. The feasibility predicate is monotonic: higher speed never increases travel time.

---

## Complexity Analysis
- **Time Complexity**: `O(n log U)`, where `U` is the speed search bound
- **Space Complexity**: `O(1)`
