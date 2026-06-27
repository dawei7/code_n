# Maximum Number of Jumps to Reach the Last Index

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2770 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming |
| Official Link | [maximum-number-of-jumps-to-reach-the-last-index](https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/) |

## Problem Description & Examples
### Goal
Given an array of integers representing heights and a target jump threshold, determine the maximum number of jumps required to travel from the first index to the last index. A jump from index `i` to index `j` is valid if `i < j` and the absolute difference between the heights at these indices is within the range `[-target, target]`. If it is impossible to reach the last index, return -1.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the heights at each position.
- `target`: An integer representing the maximum allowed absolute difference between heights for a valid jump.

**Return value**

- An integer representing the maximum number of jumps to reach the last index, or -1 if the destination is unreachable.

### Examples
**Example 1**

- Input: `nums = [1, 3, 6, 4, 1, 2], target = 2`
- Output: `3`

**Example 2**

- Input: `nums = [1, 3, 6, 4, 1, 2], target = 3`
- Output: `5`

**Example 3**

- Input: `nums = [1, 0, 2], target = 1`
- Output: `-1`

---

## Underlying Base Algorithm(s)
Dynamic Programming (Linear DP). We maintain an array `dp` where `dp[i]` stores the maximum jumps to reach index `i`. We iterate through each index `i` and check all previous indices `j < i` to see if a jump is valid. If valid, we update `dp[i] = max(dp[i], dp[j] + 1)`.

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`, where `n` is the length of the input array, due to the nested loops checking all previous indices for each position.
- **Space Complexity**: `O(n)` to store the DP array tracking the maximum jumps for each index.
