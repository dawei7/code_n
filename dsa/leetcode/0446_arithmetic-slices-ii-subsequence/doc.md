# Arithmetic Slices II - Subsequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 446 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/arithmetic-slices-ii-subsequence/) |

## Problem Description
### Goal
Given an integer array, choose index subsequences of at least three elements while preserving original index order. A subsequence is arithmetic when every difference between consecutive selected values is identical; the common difference may be positive, negative, or zero.

Return the number of qualifying index subsequences. Selected positions need not be contiguous, and different index choices count separately even when duplicate values produce the same value sequence. Longer arithmetic subsequences count once as complete selections and also contain shorter selections that may count independently. Use sufficiently wide arithmetic for value differences and the total count.

### Function Contract
**Inputs**

- `nums`: an integer array from which subsequences retain original index order

**Return value**

- Return the number of arithmetic subsequences of length at least three; equal value sequences use common difference zero.

### Examples
**Example 1**

- Input: `nums = [2, 4, 6, 8, 10]`
- Output: `7`

**Example 2**

- Input: `nums = [7, 7, 7, 7, 7]`
- Output: `16`

**Example 3**

- Input: `nums = [1, 2]`
- Output: `0`
