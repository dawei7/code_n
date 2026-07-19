# Longest Increasing Subsequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 300 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-increasing-subsequence/) |

## Problem Description
### Goal
Given a nonempty integer array, choose a subsequence by deleting any number of elements while preserving the original order of those retained. The chosen values must be strictly increasing from one selected position to the next.

Return the maximum possible subsequence length. Selected elements do not need to occupy consecutive indices, but their indices cannot be reordered. Equal values do not extend a strictly increasing sequence, and negative values follow the same comparison rule. The task returns only the optimal length, not a particular subsequence, and the required solution should achieve the specified $O(n \log n)$ time.

### Function Contract
**Inputs**

- `nums`: a nonempty list of integers

**Return value**

The length of the longest strictly increasing subsequence. Selected elements need not be contiguous.

### Examples
**Example 1**

- Input: `nums = [10,9,2,5,3,7,101,18]`
- Output: `4`

**Example 2**

- Input: `nums = [0,1,0,3,2,3]`
- Output: `4`

**Example 3**

- Input: `nums = [7,7,7,7]`
- Output: `1`
