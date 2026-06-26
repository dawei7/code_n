# Shortest Subarray to be Removed to Make Array Sorted

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1574 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Binary Search, Stack, Monotonic Stack |
| Official Link | [shortest-subarray-to-be-removed-to-make-array-sorted](https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/) |

## Problem Description & Examples
### Goal
Remove one contiguous subarray, possibly empty, so the remaining elements are in
nondecreasing order. Minimize the removed length.

### Function Contract
**Inputs**

- `arr`: an integer array.

**Return value**

The shortest length that can be removed.

### Examples
**Example 1**

- Input: `arr = [1, 2, 3, 10, 4, 2, 3, 5]`
- Output: `3`

**Example 2**

- Input: `arr = [5, 4, 3, 2, 1]`
- Output: `4`

**Example 3**

- Input: `arr = [1, 2, 3]`
- Output: `0`

---

## Underlying Base Algorithm(s)
Find the longest sorted prefix and sorted suffix. Removing everything after the
prefix or before the suffix gives an initial answer. Then use two pointers to
merge a prefix end with a compatible suffix start and minimize the gap removed
between them.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`.
- **Space Complexity**: `O(1)`.
