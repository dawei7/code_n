# Length of the Longest Subsequence That Sums to Target

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2915 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming |
| Official Link | [length-of-the-longest-subsequence-that-sums-to-target](https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/) |

## Problem Description & Examples
### Goal
Given an array of integers and a target sum, determine the maximum number of elements that can be selected from the array such that their sum equals the target. If no such subsequence exists, return -1.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the available numbers.
- `target`: An integer representing the required sum.

**Return value**

- An integer representing the length of the longest subsequence that sums to `target`, or -1 if no such subsequence exists.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4, 5], target = 9`
- Output: `3` (e.g., [1, 3, 5] or [2, 3, 4])

**Example 2**

- Input: `nums = [4, 1, 3, 2, 1, 5], target = 7`
- Output: `4` (e.g., [4, 1, 1, 1] is not possible, but [1, 1, 2, 3] sums to 7)

**Example 3**

- Input: `nums = [1, 1, 5, 4, 5], target = 3`
- Output: `-1`

---

## Underlying Base Algorithm(s)
This is a variation of the **0/1 Knapsack Problem**. Specifically, it is a dynamic programming problem where we maintain an array `dp` of size `target + 1`. `dp[i]` stores the maximum length of a subsequence that sums to `i`. We initialize `dp[0] = 0` and all other indices to negative infinity to represent unreachable sums. For each number in the input, we update the `dp` table in reverse to ensure each element is used at most once.

---

## Complexity Analysis
- **Time Complexity**: `O(n * target)`, where `n` is the length of the input array. We iterate through each number and update the DP table of size `target`.
- **Space Complexity**: `O(target)`, as we only maintain a 1D array of size `target + 1` to store the maximum lengths.
