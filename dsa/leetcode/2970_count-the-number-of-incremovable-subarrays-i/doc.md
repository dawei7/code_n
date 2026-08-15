# Count the Number of Incremovable Subarrays I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2970 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Two Pointers, Binary Search, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-i/) |

## Problem Description

### Goal

You are given a 0-indexed array `nums` of positive integers. A subarray is a
contiguous, non-empty sequence of its elements.

Call a subarray *incremovable* when deleting exactly that subarray leaves the
remaining elements in strictly increasing order. The retained elements keep
their original relative order, so values on opposite sides of the deletion
become adjacent. An empty remaining array is considered strictly increasing.

Return the total number of incremovable subarrays of `nums`. Different choices
of left and right endpoints count separately, even when their values happen to
be equal.

### Function Contract

**Inputs**

- `nums`: the positive integers in their original array order

Let $N=\lvert\texttt{nums}\rvert$. The contract guarantees $1\le N\le50$ and
$1\le\texttt{nums[i]}\le50$.

**Return value**

The number of non-empty contiguous subarrays whose removal leaves a strictly
increasing sequence.

### Examples

#### Example 1

- **Input:** `nums = [1,2,3,4]`
- **Output:** `10`
- **Explanation:** Removing any of the ten non-empty subarrays leaves a strictly increasing array.

#### Example 2

- **Input:** `nums = [6,5,7,8]`
- **Output:** `7`
- **Explanation:** Exactly seven endpoint pairs remove the descent or one of its surrounding portions while preserving strict increase.

#### Example 3

- **Input:** `nums = [8,7,6,6]`
- **Output:** `3`
- **Explanation:** The valid deletions are the whole array and the two length-three subarrays; retaining the equal `6` values would not be strictly increasing.
