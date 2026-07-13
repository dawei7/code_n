# Missing Element in Sorted Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1060 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [missing-element-in-sorted-array](https://leetcode.com/problems/missing-element-in-sorted-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/missing-element-in-sorted-array/).

### Goal
Given a strictly increasing sorted array, return the `k`th missing number after the first array element when counting upward through the integer line.

### Function Contract
**Inputs**

- `nums`: Strictly increasing list of integers.
- `k`: Positive missing-count index.

**Return value**

The `k`th missing integer.

### Examples
**Example 1**

- Input: `nums = [4, 7, 9, 10], k = 1`
- Output: `5`

**Example 2**

- Input: `nums = [4, 7, 9, 10], k = 3`
- Output: `8`

**Example 3**

- Input: `nums = [1, 2, 4], k = 3`
- Output: `6`

---

## Solution
### Approach
For index `i`, the count of missing numbers between `nums[0]` and `nums[i]` is `nums[i] - nums[0] - i`. Use binary search to find the first index where this count is at least `k`.

If the total missing count before the last element is smaller than `k`, the answer lies after the array. Otherwise, use the previous index and the remaining missing count to compute the exact value.

### Complexity Analysis
- **Time Complexity**: `O(log n)`.
- **Space Complexity**: `O(1)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
