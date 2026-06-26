# Minimum Skips to Arrive at Meeting On Time

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1883 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming |
| Official Link | [minimum-skips-to-arrive-at-meeting-on-time](https://leetcode.com/problems/minimum-skips-to-arrive-at-meeting-on-time/) |

## Problem Description & Examples
### Goal
Travel a sequence of roads at a fixed speed. After each road except the last, you normally wait until the next integer hour before continuing. You may skip some waits. Find the fewest skips needed to arrive within `hoursBefore`.

### Function Contract
**Inputs**

- `dist`: road distances in order.
- `speed`: the constant travel speed.
- `hoursBefore`: the latest allowed arrival time.

**Return value**

Return the minimum number of skipped waits, or `-1` if arriving on time is impossible.

### Examples
**Example 1**

- Input: `dist = [1,3,2], speed = 4, hoursBefore = 2`
- Output: `1`

**Example 2**

- Input: `dist = [7,3,5,5], speed = 2, hoursBefore = 10`
- Output: `2`

**Example 3**

- Input: `dist = [7,3,5,5], speed = 1, hoursBefore = 10`
- Output: `-1`

---

## Underlying Base Algorithm(s)
Use dynamic programming over roads and number of skips. Store elapsed distance units rather than floating hours to avoid precision issues. After each non-final road, either round up to the next multiple of `speed` if not skipping, or keep the exact elapsed distance if skipping. The smallest skip count whose final elapsed distance is at most `hoursBefore * speed` is the answer.

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n)`
