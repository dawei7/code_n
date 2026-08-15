# Minimum Sum of Mountain Triplets II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2909 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-sum-of-mountain-triplets-ii/) |

## Problem Description

### Goal

Given a 0-indexed integer array `nums`, call three indices $(i,j,k)$ a mountain triplet when $i<j<k$ and the middle value is strictly greater than both selected side values. Thus both `nums[i] < nums[j]` and `nums[k] < nums[j]` must hold. The three positions may be separated by any number of other elements.

Compute `nums[i] + nums[j] + nums[k]` for each valid mountain triplet and return the minimum possible sum. If no middle index has a strictly smaller value somewhere before it and another strictly smaller value somewhere after it, return `-1`. The array can contain up to $10^5$ values, so repeatedly rescanning either side for every middle index is not efficient enough.

### Function Contract

**Inputs**

- `nums`: An integer array of length $n$, where $3\le n\le 10^5$ and $1\le\texttt{nums}[i]\le 10^8$.

**Return value**

Return the minimum sum of any mountain triplet. Return `-1` when no mountain triplet exists.

### Examples

#### Example 1

- **Input:** `nums = [8, 6, 1, 5, 3]`
- **Output:** `9`
- **Explanation:** Indices `[2, 3, 4]` contain `[1, 5, 3]`, whose middle is strictly larger than both sides and whose sum is $9$.

#### Example 2

- **Input:** `nums = [5, 4, 8, 7, 10, 2]`
- **Output:** `13`
- **Explanation:** Indices `[1, 3, 5]` contain `[4, 7, 2]`. Their sum is $13$, the minimum over all mountain triplets.

#### Example 3

- **Input:** `nums = [6, 5, 4, 3, 4, 5]`
- **Output:** `-1`
- **Explanation:** No middle index has a strictly smaller value on both sides.
