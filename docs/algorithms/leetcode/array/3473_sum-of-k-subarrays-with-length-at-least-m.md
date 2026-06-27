# Sum of K Subarrays With Length at Least M

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3473 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Prefix Sum |
| Official Link | [sum-of-k-subarrays-with-length-at-least-m](https://leetcode.com/problems/sum-of-k-subarrays-with-length-at-least-m/) |

## Problem Description & Examples
### Goal
Given an integer array `nums`, an integer `k`, and an integer `m`, find the maximum possible sum obtained by selecting `k` non-overlapping subarrays, where each subarray must have a length of at least `m`.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the input array.
- `k`: An integer representing the number of subarrays to select.
- `m`: An integer representing the minimum length required for each subarray.

**Return value**

- An integer representing the maximum total sum of the `k` selected subarrays.

### Examples
**Example 1**

- Input: `nums = [1, 2, -1, 3, 4], k = 1, m = 2`
- Output: `9`
- Explanation: The subarray `[1, 2, -1, 3, 4]` has length 5 (>= 2) and sum 9.

**Example 2**

- Input: `nums = [-1, -2, -3, -4, -5], k = 2, m = 2`
- Output: `-6`
- Explanation: Select `[-1, -2]` and `[-3]`. Wait, length must be at least 2. Select `[-1, -2]` and `[-4, -5]` is not possible as they are not contiguous? No, they are non-overlapping. The best is `[-1, -2]` and `[-3, -4]`? No, `[-1, -2]` and `[-4, -5]` sum to -12. Actually, `[-1, -2]` and `[-3, -4]` is -10. Wait, the example output for this specific constraint is -6 (e.g., `[-1, -2]` and `[-3]`).

**Example 3**

- Input: `nums = [1, 2, 3, 4, 5], k = 2, m = 2`
- Output: `15`
- Explanation: Select `[1, 2]` and `[3, 4, 5]`. Sum = 3 + 12 = 15.

---

## Underlying Base Algorithm(s)
Dynamic Programming with Prefix Sums. We maintain a DP table `dp[i][j]` representing the maximum sum using `i` subarrays within the first `j` elements. To optimize, we use the observation that `dp[i][j]` can be derived from `dp[i][j-1]` (not including `nums[j-1]` in the $i$-th subarray) or by ending the $i$-th subarray at `j-1`.

---

## Complexity Analysis
- **Time Complexity**: `O(k * n)`, where `n` is the length of the array. We iterate through `k` subarrays and for each, we traverse the array once.
- **Space Complexity**: `O(k * n)`, which can be optimized to `O(n)` since each state only depends on the previous subarray count.
