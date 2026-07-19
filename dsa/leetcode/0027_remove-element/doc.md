# Remove Element

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 27 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Two Pointers |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/remove-element/) |

## Problem Description
### Goal
Given an integer array `nums` and a value `val`, remove every occurrence of that value in place. The array's physical length need not shrink; instead, place all retained values in a prefix and treat positions beyond that prefix as irrelevant.

The native method returns the number `k` of retained elements, and its first `k` entries may appear in any order. The app-friendly contract uses a stable compaction and returns the retained prefix itself for direct checking. An empty array or an array containing only `val` therefore produces an empty retained result.

### Function Contract
**Inputs**

- `nums`: `List[int]`
- `val`: `int`

**Return value**

A `List[int]` containing all values unequal to `val` in original order. The platform artifact writes this prefix into `nums` and returns its length.

### Examples
**Example 1**

- Input: `nums = [3, 2, 2, 3], val = 3`
- Output: `[2, 2]`

**Example 2**

- Input: `nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2`
- Output: `[0, 1, 3, 0, 4]`

**Example 3**

- Input: `nums = [], val = 1`
- Output: `[]`
