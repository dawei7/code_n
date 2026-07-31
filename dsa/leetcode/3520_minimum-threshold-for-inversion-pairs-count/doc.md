# Minimum Threshold for Inversion Pairs Count

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3520 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Divide and Conquer, Binary Indexed Tree, Segment Tree, Merge Sort |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-threshold-for-inversion-pairs-count/) |

## Problem Description
### Goal
Given an integer array `nums`, an inversion pair is a pair of indices $(i,j)$ with $i<j$ and `nums[i] > nums[j]`. A threshold $x$ further restricts an inversion pair by requiring its value difference to be at most $x$, so `nums[i] - nums[j] <= x` must also hold.

Find the minimum integer threshold for which at least `k` inversion pairs satisfy all three conditions. If the array contains fewer than `k` inversion pairs even when every positive difference is allowed, return `-1`.

### Function Contract
**Inputs**

- `nums`: An array of positive integers.
- `k`: The minimum number of qualifying inversion pairs required.

Let $n=\lvert\texttt{nums}\rvert$ and $R=\max(\texttt{nums})-\min(\texttt{nums})$. The constraints are $1\le n\le 10^4$, $1\le\texttt{nums[i]}\le 10^9$, and $1\le k\le 10^9$.

**Return value**

Return the smallest integer threshold that admits at least `k` inversion pairs, or `-1` when no such threshold exists.

### Examples
**Example 1**

- Input: `nums = [1,2,3,4,3,2,1], k = 7`
- Output: `2`
- Explanation: Threshold 2 admits eight inversions, while every smaller integer threshold admits fewer than seven.

**Example 2**

- Input: `nums = [10,9,9,9,1], k = 4`
- Output: `8`
- Explanation: Difference 1 contributes the three inversions from `10` to the three `9` values. Threshold 8 additionally admits the inversions from each `9` to `1`, so it is the first threshold reaching four pairs.

**Example 3**

- Input: `nums = [1,2,3], k = 1`
- Output: `-1`
- Explanation: An ascending array has no inversion pair.
