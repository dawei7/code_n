# Maximize Win From Two Segments

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2555 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Sliding Window |
| Official Link | [maximize-win-from-two-segments](https://leetcode.com/problems/maximize-win-from-two-segments/) |

## Problem Description & Examples
### Goal
Given a sorted array of prize positions and a fixed segment length `k`, determine the maximum number of prizes you can collect by placing two non-overlapping segments of length `k` anywhere on the number line.

### Function Contract
**Inputs**

- `prizePositions`: A sorted list of integers representing the locations of prizes.
- `k`: An integer representing the length of each of the two segments.

**Return value**

- An integer representing the maximum total number of prizes that can be covered by two segments of length `k`.

### Examples
**Example 1**

- Input: `prizePositions = [1,1,2,2,3,3,5], k = 2`
- Output: `7`

**Example 2**

- Input: `prizePositions = [1,2,3,4], k = 0`
- Output: `2`

**Example 3**

- Input: `prizePositions = [5,5,5,5], k = 4`
- Output: `4`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Sliding Window** approach combined with **Dynamic Programming** (or prefix maximums). First, we calculate the maximum number of prizes a single segment of length `k` can cover ending at each index `i`. Then, we iterate through the array to find the best pair of non-overlapping segments by keeping track of the maximum prizes covered by a segment ending at or before the start of the current segment.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the number of prizes. We perform a single pass to calculate window counts and another pass to find the optimal pair.
- **Space Complexity**: `O(n)` to store the maximum prizes covered by a segment ending at each index.
