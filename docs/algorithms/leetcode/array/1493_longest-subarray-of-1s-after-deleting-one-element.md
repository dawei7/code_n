# Longest Subarray of 1's After Deleting One Element

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1493 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Sliding Window |
| Official Link | [longest-subarray-of-1s-after-deleting-one-element](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/) |

## Problem Description & Examples
### Goal
Delete exactly one element, then find the longest contiguous subarray containing only `1`s.

### Function Contract
**Inputs**

- `nums`: a binary array.

**Return value**

The maximum length of all-ones subarray after one deletion.

### Examples
**Example 1**

- Input: `nums = [1,1,0,1]`
- Output: `3`

**Example 2**

- Input: `nums = [0,1,1,1,0,1,1,0,1]`
- Output: `5`

**Example 3**

- Input: `nums = [1,1,1]`
- Output: `2`

---

## Underlying Base Algorithm(s)
Sliding window with at most one zero. The window length minus one represents deleting one element.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
