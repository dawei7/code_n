# Create Maximum Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 321 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Two Pointers, Stack, Greedy, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/create-maximum-number/) |

## Problem Description
### Goal
Given two arrays of decimal digits, select a total of exactly `k` occurrences from their combined positions. Within the digits chosen from each individual array, preserve the original relative order, but interleave selections from the two arrays in any way.

Return the lexicographically largest possible length-`k` digit sequence. Every occurrence can be used at most once, duplicate digit values at different positions remain distinct choices, and no reordering is allowed inside either source. Compare candidates from left to right by digit value. The required length may draw all digits from one array or split them between both, subject to availability.

### Function Contract
**Inputs**

- `nums1`: the first digit sequence
- `nums2`: the second digit sequence
- `k`: the required output length

**Return value**

The lexicographically largest valid list of `k` digits.

### Examples
**Example 1**

- Input: `nums1 = [3,4,6,5], nums2 = [9,1,2,5,8,3], k = 5`
- Output: `[9,8,6,5,3]`

**Example 2**

- Input: `nums1 = [6,7], nums2 = [6,0,4], k = 5`
- Output: `[6,7,6,0,4]`

**Example 3**

- Input: `nums1 = [3,9], nums2 = [8,9], k = 3`
- Output: `[9,8,9]`
