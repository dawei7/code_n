# Find the Count of Monotonic Pairs II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3251 |
| Difficulty | Hard |
| Topics | Array, Math, Dynamic Programming, Combinatorics, Prefix Sum |
| Official Link | [find-the-count-of-monotonic-pairs-ii](https://leetcode.com/problems/find-the-count-of-monotonic-pairs-ii/) |

## Problem Description & Examples
### Goal
Given an array of non-negative integers `nums`, determine the number of pairs of arrays `(arr1, arr2)` such that `arr1` is non-decreasing, `arr2` is non-increasing, and for every index `i`, `arr1[i] + arr2[i] == nums[i]`. The result should be returned modulo 10^9 + 7.

### Function Contract
**Inputs**

- `nums`: A list of non-negative integers where `0 <= nums[i] <= 1000`.

**Return value**

- An integer representing the total count of valid pairs `(arr1, arr2)` modulo 10^9 + 7.

### Examples
**Example 1**

- Input: `nums = [2, 3, 2]`
- Output: `4`

**Example 2**

- Input: `nums = [5, 5, 5, 5]`
- Output: `126`

**Example 3**

- Input: `nums = [1]`
- Output: `2`

---

## Underlying Base Algorithm(s)
The problem is solved using Dynamic Programming optimized with Prefix Sums. Let `dp[i][j]` be the number of ways to choose `arr1[i] = j`. The constraints `arr1[i] >= arr1[i-1]` and `arr2[i] <= arr2[i-1]` (which implies `nums[i] - arr1[i] <= nums[i-1] - arr1[i-1]`) lead to the condition `arr1[i-1] <= min(j, j - (nums[i] - nums[i-1]))`. By maintaining a prefix sum of the previous DP row, we can calculate the transition in O(1) time, reducing the overall complexity from O(N * max(nums)^2) to O(N * max(nums)).

---

## Complexity Analysis
- **Time Complexity**: O(N * M), where N is the length of `nums` and M is the maximum value in `nums`.
- **Space Complexity**: O(M), as we only need the current and previous rows of the DP table.
