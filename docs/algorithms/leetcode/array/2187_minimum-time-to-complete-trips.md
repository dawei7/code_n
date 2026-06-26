# Minimum Time to Complete Trips

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2187 |
| Difficulty | Medium |
| Topics | Array, Binary Search |
| Official Link | [minimum-time-to-complete-trips](https://leetcode.com/problems/minimum-time-to-complete-trips/) |

## Problem Description & Examples
### Goal
Find the earliest time by which a fleet of buses can complete at least a target number of trips. Bus `i` takes `time[i]` units per trip and begins another trip immediately after finishing one; all buses operate concurrently.

### Function Contract
**Inputs**

- `time`: positive trip durations for the buses.
- `totalTrips`: the required combined number of completed trips.

**Return value**

The minimum whole-number time at which at least `totalTrips` have finished.

### Examples
**Example 1**

- Input: `time = [1, 2, 3]`, `totalTrips = 5`
- Output: `3`

**Example 2**

- Input: `time = [2]`, `totalTrips = 1`
- Output: `2`

**Example 3**

- Input: `time = [5, 10, 10]`, `totalTrips = 9`
- Output: `25`

---

## Underlying Base Algorithm(s)
Binary-search time `t`. By then, bus `i` has completed `floor(t / time[i])` trips, so `t` is feasible when their sum reaches `totalTrips`. Feasibility is monotonic, and `min(time) * totalTrips` is a valid upper bound.

---

## Complexity Analysis
- **Time Complexity**: `O(n log(min(time) * totalTrips))`
- **Space Complexity**: `O(1)`
