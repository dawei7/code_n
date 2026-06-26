# Number of Sub-arrays With Odd Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1524 |
| Difficulty | Medium |
| Topics | Array, Math, Dynamic Programming, Prefix Sum |
| Official Link | [number-of-sub-arrays-with-odd-sum](https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/) |

## Problem Description & Examples
### Goal
Count the contiguous subarrays whose sum is odd.

### Function Contract
**Inputs**

- `arr`: an integer array.

**Return value**

The number of odd-sum subarrays modulo `1_000_000_007`.

### Examples
**Example 1**

- Input: `arr = [1, 3, 5]`
- Output: `4`

**Example 2**

- Input: `arr = [2, 4, 6]`
- Output: `0`

**Example 3**

- Input: `arr = [1, 2, 3, 4]`
- Output: `6`

---

## Underlying Base Algorithm(s)
Track prefix-sum parity. A subarray has odd sum when its ending prefix parity is
different from its starting prefix parity, so keep counts of even and odd
prefixes seen so far and add the opposite count at each element.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`.
- **Space Complexity**: `O(1)`.
