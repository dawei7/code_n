# Remove Duplicates from Sorted Array II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 80 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/) |

## Problem Description
### Goal
You are given a nonempty integer array sorted in non-decreasing order. Compact it in place so each unique element appears at most twice in the useful leading portion, preserving relative order and retaining both copies whenever at least two originally exist.

The native method returns the retained length `k`, and only `nums[:k]` is significant afterward; constant auxiliary space is required. The cOde(n) adapter returns that prefix itself for direct inspection. Values occurring once remain once, while every longer duplicate run is shortened to two.

### Function Contract
**Inputs**

- `nums`: a nonempty sorted `List[int]`

**Return value**

The retained prefix in the app adapter. The platform method returns its length and leaves those values in `nums[:length]`.

### Examples
**Example 1**

- Input: `nums = [1,1,1,2,2,3]`
- Output prefix: `[1,1,2,2,3]`

**Example 2**

- Input: `nums = [0,0,1,1,1,1,2,3,3]`
- Output prefix: `[0,0,1,1,2,3,3]`

**Example 3**

- Input: `nums = [5]`
- Output prefix: `[5]`
