# Minimum Subarrays in a Valid Split

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2464 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-subarrays-in-a-valid-split/) |

## Problem Description

### Goal

You are given an integer array `nums`. Split it into contiguous, non-empty subarrays so that every original element belongs to exactly one part. A split is valid only when, for each part, the greatest common divisor of that part's first and last elements is greater than $1$. Values between those endpoints do not affect whether the part is valid.

Return the minimum possible number of subarrays in a valid split. If no partition satisfies the endpoint condition for every part, return `-1`. The greatest common divisor of two integers is their largest shared positive divisor.

### Function Contract

**Inputs**

- `nums`: A list of positive integers to partition without reordering or omission.

The constraints are $1\le\lvert\texttt{nums}\rvert\le1000$ and $1\le\texttt{nums[i]}\le10^5$.

**Return value**

- The fewest contiguous parts whose endpoint GCDs all exceed $1$, or `-1` when no valid split exists.

### Examples

#### Example 1

- **Input:** `nums = [2, 6, 3, 4, 3]`
- **Output:** `2`
- **Explanation:** `[2, 6]` has endpoint GCD `2`, and `[3, 4, 3]` has endpoint GCD `3`.

#### Example 2

- **Input:** `nums = [3, 5]`
- **Output:** `2`
- **Explanation:** Each value forms a valid singleton, and the two values cannot be endpoints of one valid part.

#### Example 3

- **Input:** `nums = [1, 2, 1]`
- **Output:** `-1`
- **Explanation:** A part starting or ending with `1` has endpoint GCD `1`, so no valid partition covers the array.
