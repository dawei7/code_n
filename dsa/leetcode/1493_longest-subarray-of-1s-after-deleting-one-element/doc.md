# Longest Subarray of 1's After Deleting One Element

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1493 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Sliding Window |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/) |

## Problem Description
### Goal

Given a binary array `nums`, delete exactly one element from it. After that deletion, inspect the remaining array for contiguous subarrays containing only `1` values.

Return the greatest possible length of such an all-ones subarray. The deleted element may be either `0` or `1`; in particular, an input containing only ones must still lose one element. If no `1` remains in a useful run, return `0`.

### Function Contract
**Inputs**

Let $N$ be the length of `nums`.

- `nums`: a binary list with $1 \le N \le 10^5$.
- Every entry is either `0` or `1`.

**Return value**

Return the maximum number of consecutive ones obtainable after deleting exactly one array element.

### Examples
**Example 1**

- Input: `nums = [1,1,0,1]`
- Output: `3`
- Explanation: Deleting the zero joins the runs `[1,1]` and `[1]`.

**Example 2**

- Input: `nums = [0,1,1,1,0,1,1,0,1]`
- Output: `5`
- Explanation: Deleting the zero between the three-one and two-one runs creates five consecutive ones.

**Example 3**

- Input: `nums = [1,1,1]`
- Output: `2`
- Explanation: A deletion is mandatory, so one of the three ones must be removed.
