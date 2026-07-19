# Remove Duplicates from Sorted Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 26 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Two Pointers |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) |

## Problem Description
### Goal
You are given a nonempty integer array `nums` sorted in non-decreasing order. Modify it in place so that each unique element appears exactly once in the leading portion, retaining the elements' relative order. Values beyond that useful prefix do not matter.

The native method returns the number of unique elements `k`, and the first `k` positions must then contain those elements in the order in which they occur. It may use only constant auxiliary storage. For direct app testing, `solve` returns that same retained prefix, making both its content and `k` observable.

### Function Contract
**Inputs**

- `nums`: non-empty nondecreasing `List[int]`

**Return value**

A `List[int]` containing the distinct values in sorted order. The official platform artifact instead returns this prefix's length after writing it into `nums`.

### Examples
**Example 1**

- Input: `nums = [1, 1, 2]`
- Output: `[1, 2]`

**Example 2**

- Input: `nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]`
- Output: `[0, 1, 2, 3, 4]`

**Example 3**

- Input: `nums = [7]`
- Output: `[7]`
