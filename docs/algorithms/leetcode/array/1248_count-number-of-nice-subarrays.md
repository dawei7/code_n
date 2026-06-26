# Count Number of Nice Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1248 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Math, Sliding Window, Prefix Sum |
| Official Link | [count-number-of-nice-subarrays](https://leetcode.com/problems/count-number-of-nice-subarrays/) |

## Problem Description & Examples
### Goal
Count contiguous subarrays containing exactly `k` odd numbers.

### Function Contract
**Inputs**

- `nums`: integer array.
- `k`: required number of odd elements.

**Return value**

The number of subarrays with exactly `k` odd values.

### Examples
**Example 1**

- Input: `nums = [1,1,2,1,1]`, `k = 3`
- Output: `2`

**Example 2**

- Input: `nums = [2,4,6]`, `k = 1`
- Output: `0`

**Example 3**

- Input: `nums = [2,2,2,1,2,2,1,2,2,2]`, `k = 2`
- Output: `16`

---

## Underlying Base Algorithm(s)
Prefix sum frequency counting.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` in the worst case.
