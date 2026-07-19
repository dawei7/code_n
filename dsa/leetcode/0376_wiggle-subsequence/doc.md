# Wiggle Subsequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 376 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/wiggle-subsequence/) |

## Problem Description
### Goal
Given an integer array, choose a subsequence by deleting any number of elements while preserving the retained indices' order. It is a wiggle sequence when every consecutive difference is nonzero and the signs of those differences alternate positive, negative, positive, or negative, positive, negative.

Return the maximum possible wiggle subsequence length. A one-value sequence is valid, and a two-value sequence is valid when its values differ. Equal adjacent selected values produce a zero difference and cannot extend the pattern. Selected elements need not be contiguous. A one-element input returns `1`. Return only the maximum length, not the subsequence, and meet the follow-up target of $O(n)$ time.

### Function Contract
**Inputs**

- `nums`: a list of integers

**Return value**

- The length of the longest wiggle subsequence. A one-value subsequence has length one.

### Examples
**Example 1**

- Input: `nums = [1,7,4,9,2,5]`
- Output: `6`

**Example 2**

- Input: `nums = [1,17,5,10,13,15,10,5,16,8]`
- Output: `7`

**Example 3**

- Input: `nums = [1,2,3,4,5,6,7,8,9]`
- Output: `2`
