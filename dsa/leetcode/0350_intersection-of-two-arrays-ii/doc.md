# Intersection of Two Arrays II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 350 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Two Pointers, Binary Search, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/intersection-of-two-arrays-ii/) |

## Problem Description
### Goal
Given two integer arrays, compute their multiset intersection. For each value, the output may use only occurrences supported independently by both inputs rather than treating repeated values as one set member.

If a value occurs $a$ times in the first array and $b$ times in the second, include it exactly $\min(a,b)$ times. Return all such occurrences in any order. Values appearing in only one array contribute nothing, and each input occurrence can be matched at most once. If no value is shared, the result is empty; otherwise duplicates must be preserved up to the shared multiplicity.

### Function Contract
**Inputs**

- `nums1`: the first integer array
- `nums2`: the second integer array

**Return value**

- A list containing each shared value with the multiplicity supported by both arrays, in any order.

### Examples
**Example 1**

- Input: `nums1 = [1, 2, 2, 1], nums2 = [2, 2]`
- Output: `[2, 2]`

**Example 2**

- Input: `nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]`
- Output: `[4, 9]`

**Example 3**

- Input: `nums1 = [1, 2], nums2 = [1, 1]`
- Output: `[1]`
