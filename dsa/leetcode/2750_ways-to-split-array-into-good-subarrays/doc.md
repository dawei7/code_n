# Ways to Split Array Into Good Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2750 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/ways-to-split-array-into-good-subarrays/) |

## Problem Description

### Goal

You are given a binary array `nums`. A non-empty contiguous subarray is good when it contains exactly one element equal to `1`. Split the entire array into one or more contiguous, non-empty pieces, with every original element belonging to exactly one piece and the piece order unchanged.

Count how many different placements of split boundaries make every resulting subarray good. If the array contains no `1`, no valid split exists. Return the count modulo $10^9+7$.

### Function Contract

Let $n$ be the length of `nums`.

**Inputs**

- `nums`: A binary array where $1 \le n \le 10^5$ and every value is either `0` or `1`.

**Return value**

Return the number of ways to partition the entire array into good subarrays, modulo $10^9+7$.

### Examples

#### Example 1

- **Input:** `nums = [0,1,0,0,1]`
- **Output:** `3`
- **Explanation:** The single boundary between the two `1` values can follow any of the three positions from the first `1` through the last intervening `0`.

#### Example 2

- **Input:** `nums = [0,1,0]`
- **Output:** `1`
- **Explanation:** The whole array is already one good subarray.
