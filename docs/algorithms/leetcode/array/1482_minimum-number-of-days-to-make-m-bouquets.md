# Minimum Number of Days to Make m Bouquets

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1482 |
| Difficulty | Medium |
| Topics | Array, Binary Search |
| Official Link | [minimum-number-of-days-to-make-m-bouquets](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/) |

## Problem Description & Examples
### Goal
Find the earliest day when at least `m` bouquets can be made, each using `k` adjacent flowers that have bloomed by that day.

### Function Contract
**Inputs**

- `bloomDay`: bloom day for each flower.
- `m`: required number of bouquets.
- `k`: adjacent flowers needed per bouquet.

**Return value**

The minimum feasible day, or `-1` if there are not enough flowers.

### Examples
**Example 1**

- Input: `bloomDay = [1,10,3,10,2], m = 3, k = 1`
- Output: `3`

**Example 2**

- Input: `bloomDay = [1,10,3,10,2], m = 3, k = 2`
- Output: `-1`

**Example 3**

- Input: `bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3`
- Output: `12`

---

## Underlying Base Algorithm(s)
Binary search on the day. A feasibility scan counts consecutive bloomed flowers and forms a bouquet whenever the consecutive count reaches `k`.

---

## Complexity Analysis
- **Time Complexity**: `O(n log D)`, where `D` is the bloom-day range.
- **Space Complexity**: `O(1)`
