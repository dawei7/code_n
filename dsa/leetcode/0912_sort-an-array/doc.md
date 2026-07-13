# Sort an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 912 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Divide and Conquer, Sorting, Heap (Priority Queue), Merge Sort, Bucket Sort, Radix Sort, Counting Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [sort-an-array](https://leetcode.com/problems/sort-an-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/sort-an-array/).

### Goal
Given an array of integers `nums`, sort the array in ascending order and return it.

You must solve the problem **without using the built-in sort functions**. Implement merge sort or similar O(n log n) algorithm.

### Function Contract
**Inputs**

- `nums`: List[int]

**Return value**

List[int] - sorted array

### Examples
**Example 1**

- Input: `nums = [5, 2, 3, 1]`
- Output: `[1, 2, 3, 5]`

**Example 2**

- Input: `nums = [5, 1, 1, 2, 0, 0]`
- Output: `[0, 0, 1, 1, 2, 5]`

**Example 3**

- Input: `nums = [-1, 2, -8, -10]`
- Output: `[-10, -8, -1, 2]`

---

## Solution
### Approach
- [Two Sum / hash lookup](hash_01_two-sum.md)
- [Grouping by hash key](hash_04_group-anagrams.md)
- [Set-based sequence reasoning](hash_06_longest-consecutive-sequence.md)

### Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(1)` auxiliary space, excluding the output object unless the output itself is the constructed result.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
