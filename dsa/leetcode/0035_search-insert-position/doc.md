# Search Insert Position

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 35 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/search-insert-position/) |

## Problem Description
### Goal
You are given a sorted array of distinct integers and a target value. If the target already appears, return its zero-based index. Otherwise identify the position where inserting it would preserve the array's sorted order.

Equivalently, return the first index whose current value is at least `target`; if every value is smaller, return `len(nums)`. Insertion before the first element and after the last are both valid outcomes. The required logarithmic running time calls for exploiting the sorted order rather than scanning from one end.

### Function Contract
**Inputs**

- `nums`: strictly increasing `List[int]`
- `target`: `int`

**Return value**

The first index whose value is at least target, or `len(nums)` when all values are smaller.

### Examples
**Example 1**

- Input: `nums = [1, 3, 5, 6], target = 5`
- Output: `2`

**Example 2**

- Input: `nums = [1, 3, 5, 6], target = 2`
- Output: `1`

**Example 3**

- Input: `nums = [1, 3, 5, 6], target = 7`
- Output: `4`
