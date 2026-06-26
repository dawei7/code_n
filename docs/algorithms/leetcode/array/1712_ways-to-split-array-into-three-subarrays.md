# Ways to Split Array Into Three Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1712 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Binary Search, Prefix Sum |
| Official Link | [ways-to-split-array-into-three-subarrays](https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/) |

## Problem Description & Examples
### Goal
Split a non-negative array into three non-empty contiguous parts named left, middle, and right so that `sum(left) <= sum(middle) <= sum(right)`. Count all valid splits modulo `1_000_000_007`.

### Function Contract
**Inputs**

- `nums`: a list of non-negative integers.

**Return value**

Return the number of valid two-cut positions.

### Examples
**Example 1**

- Input: `nums = [1,1,1]`
- Output: `1`

**Example 2**

- Input: `nums = [1,2,2,2,5,0]`
- Output: `3`

**Example 3**

- Input: `nums = [3,2,1]`
- Output: `0`

---

## Underlying Base Algorithm(s)
Build prefix sums. For each end index of the left part, binary search the smallest middle end where `sum(middle) >= sum(left)` and the largest middle end where `sum(middle) <= sum(right)`. Because all numbers are non-negative, prefix sums are monotonic, so those ranges can also be found with two pointers.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)` with binary search, or `O(n)` with two pointers
- **Space Complexity**: `O(n)`
