# Top K Frequent Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_13` |
| Frontend ID | 347 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Divide and Conquer, Sorting, Heap (Priority Queue), Bucket Sort, Counting, Quickselect |
| Official Link | [top-k-frequent-elements](https://leetcode.com/problems/top-k-frequent-elements/) |

## Problem Description & Examples
### Goal
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. The answer can be returned in any order.

### Function Contract
**Inputs**

- `nums`: List[int]
- `k`: int

**Return value**

List[int] - the k most frequent elements

### Examples
**Example 1**

- Input: `nums = [1, 1, 1, 2, 2, 3], k = 2`
- Output: `[1, 2]`

**Example 2**

- Input: `nums = [2, 2, 1, 2], k = 2`
- Output: `[2, 1]`

**Example 3**

- Input: `nums = [1, 1, 2, 1], k = 2`
- Output: `[1, 2]`

---

## Underlying Base Algorithm(s)
- [Two Sum / hash lookup](hash_01_two-sum.md)
- [Grouping by hash key](hash_04_group-anagrams.md)
- [Set-based sequence reasoning](hash_06_longest-consecutive-sequence.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
