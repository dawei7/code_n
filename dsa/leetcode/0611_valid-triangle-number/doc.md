# Valid Triangle Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 611 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Binary Search, Greedy, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/valid-triangle-number/) |

## Problem Description
### Goal
Given an integer array `nums`, choose triplets of distinct indices and treat their values as the side lengths of a triangle. Count a triplet only when the three selected lengths can form a nondegenerate triangle, meaning every length is positive and the sum of the two shorter sides is strictly greater than the longest side.

Return the number of valid index triplets. Equal values stored at different indices represent different choices, so two triplets with the same three lengths can both count when they select different occurrences from the array.

### Function Contract
**Inputs**

- `nums`: a list of nonnegative integer side lengths

**Return value**

- The number of triples of distinct indices whose three values satisfy the triangle inequalities
- Equal values at different indices are separate choices

### Examples
**Example 1**

- Input: `nums = [2, 2, 3, 4]`
- Output: `3`

**Example 2**

- Input: `nums = [4, 2, 3, 4]`
- Output: `4`

**Example 3**

- Input: `nums = [1, 2, 3]`
- Output: `0`
