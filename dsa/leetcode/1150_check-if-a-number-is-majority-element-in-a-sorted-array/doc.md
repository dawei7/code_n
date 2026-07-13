# Check If a Number Is Majority Element in a Sorted Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1150 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [check-if-a-number-is-majority-element-in-a-sorted-array](https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/).

### Goal
Given a sorted array and a target value, determine whether the target appears more than half the array length.

### Function Contract
**Inputs**

- `nums`: Sorted list of integers.
- `target`: Value to test.

**Return value**

Boolean indicating whether `target` is a majority element.

### Examples
**Example 1**

- Input: `nums = [2, 4, 5, 5, 5, 5, 5, 6, 6], target = 5`
- Output: `true`

**Example 2**

- Input: `nums = [10, 100, 101, 101], target = 101`
- Output: `false`

**Example 3**

- Input: `nums = [1, 1, 2, 2, 2], target = 2`
- Output: `true`

---

## Solution
### Approach
Use binary search to find the first occurrence of `target`. If no occurrence exists, return `false`. Otherwise, `target` is a majority exactly when the element at index `first + len(nums) // 2` exists and is also `target`.

This works because a value that appears more than half the array must occupy the midpoint offset from its first occurrence.

### Complexity Analysis
- **Time Complexity**: `O(log n)`.
- **Space Complexity**: `O(1)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
