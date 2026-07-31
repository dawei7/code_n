# Minimum Sum of Mountain Triplets I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2908 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-sum-of-mountain-triplets-i/) |

## Problem Description
### Goal
Given a 0-indexed integer array `nums`, call three indices $(i,j,k)$ a mountain triplet when $i<j<k$ and the middle value is strictly greater than both selected side values. In other words, `nums[i] < nums[j]` and `nums[k] < nums[j]` must both hold; the side values do not need to be equal, and the indices do not need to be consecutive.

Among every mountain triplet, minimize `nums[i] + nums[j] + nums[k]`. Return that minimum sum. If no index can serve as a peak with a strictly smaller value somewhere before it and another strictly smaller value somewhere after it, return `-1`.

### Function Contract
**Inputs**

- `nums`: An integer array of length $n$, where $3\le n\le 50$ and $1\le\texttt{nums}[i]\le 50$.

**Return value**

Return the minimum sum of any mountain triplet. Return `-1` when no mountain triplet exists.

### Examples
**Example 1**

- Input: `nums = [8, 6, 1, 5, 3]`
- Output: `9`
- Explanation: Indices `[2, 3, 4]` contain `[1, 5, 3]`, whose middle is strictly larger than both sides and whose sum is $9$.

**Example 2**

- Input: `nums = [5, 4, 8, 7, 10, 2]`
- Output: `13`
- Explanation: Indices `[1, 3, 5]` contain `[4, 7, 2]`. Their sum is $13$, the minimum over all mountain triplets.

**Example 3**

- Input: `nums = [6, 5, 4, 3, 4, 5]`
- Output: `-1`
- Explanation: No middle index has a strictly smaller value on both sides.
