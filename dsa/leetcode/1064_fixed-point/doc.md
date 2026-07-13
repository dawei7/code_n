# Fixed Point

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1064 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [fixed-point](https://leetcode.com/problems/fixed-point/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/fixed-point/).

### Goal
Given a sorted array of distinct integers, return the smallest index `i` such that `arr[i] == i`. Return `-1` if no such index exists.

### Function Contract
**Inputs**

- `arr`: Sorted list of distinct integers.

**Return value**

Smallest fixed-point index, or `-1`.

### Examples
**Example 1**

- Input: `arr = [-10, -5, 0, 3, 7]`
- Output: `3`

**Example 2**

- Input: `arr = [0, 2, 5, 8, 17]`
- Output: `0`

**Example 3**

- Input: `arr = [-10, -5, 3, 4, 7, 9]`
- Output: `-1`

---

## Solution
### Approach
Because `arr` is sorted with distinct values, the function `arr[i] - i` is nondecreasing. Use binary search to find the leftmost index where `arr[i] - i >= 0`; that index is a fixed point only if `arr[i] == i`.

A linear scan also works, but binary search uses the sorted distinct property directly.

### Complexity Analysis
- **Time Complexity**: `O(log n)`.
- **Space Complexity**: `O(1)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
