# Find Subsequence of Length K With the Largest Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2099 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Sorting, Heap (Priority Queue) |
| Official Link | [find-subsequence-of-length-k-with-the-largest-sum](https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/) |

## Problem Description & Examples
### Goal
Choose a length-`k` subsequence with maximum possible sum while preserving the selected elements' original order.

### Function Contract
**Inputs**

- `nums`: an integer array.
- `k`: required subsequence length.

**Return value**

Return any maximum-sum subsequence of length `k`.

### Examples
**Example 1**

- Input: `nums = [2,1,3,3], k = 2`
- Output: `[3,3]`

**Example 2**

- Input: `nums = [-1,-2,3,4], k = 3`
- Output: `[-1,3,4]`

**Example 3**

- Input: `nums = [3,4,3,3], k = 2`
- Output: `[3,4]`

---

## Underlying Base Algorithm(s)
Select the indices of the `k` largest `(value, index)` entries using sorting or a heap. Sort those chosen indices into ascending order and return their values.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)` with sorting.
- **Space Complexity**: `O(n)`
