# Constructing Two Increasing Arrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3269 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/constructing-two-increasing-arrays/) |

## Problem Description

### Goal

You receive two arrays containing only `0` and `1`. Replace every `0` by an even positive integer and every `1` by an odd positive integer. Within each array, the replacement values must be strictly increasing from left to right.

No positive integer may be used more than once across both arrays, even at positions belonging to different arrays. Among all replacements satisfying these parity, ordering, and uniqueness rules, minimize the largest value appearing anywhere and return that minimum.

The first array may be empty, but the second contains at least one element.

### Function Contract

**Inputs**

- `nums1`: A binary list of length $n$, where $0 \le n \le 1000$.
- `nums2`: A binary list of length $m$, where $1 \le m \le 1000$.

**Return value**

- The smallest achievable maximum replacement value after both arrays become strictly increasing and every positive integer is used at most once globally.

### Examples

**Example 1**

- Input: `nums1 = [], nums2 = [1,0,1,1]`
- Output: `5`

One optimal replacement for the second array is `[1,2,3,5]`.

**Example 2**

- Input: `nums1 = [0,1,0,1], nums2 = [1,0,0,1]`
- Output: `9`

For example, `[2,3,8,9]` and `[1,4,6,7]` meet every rule.

**Example 3**

- Input: `nums1 = [0,1,0,0,1], nums2 = [0,0,0,1]`
- Output: `13`

One optimum is `[2,3,4,6,7]` together with `[8,10,12,13]`.
