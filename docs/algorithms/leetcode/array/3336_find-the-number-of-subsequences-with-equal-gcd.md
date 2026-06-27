# Find the Number of Subsequences With Equal GCD

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3336 |
| Difficulty | Hard |
| Topics | Array, Math, Dynamic Programming, Number Theory |
| Official Link | [find-the-number-of-subsequences-with-equal-gcd](https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/) |

## Problem Description & Examples
### Goal
Given an array of integers, determine the number of pairs of non-empty disjoint subsequences such that the greatest common divisor (GCD) of the elements in the first subsequence equals the GCD of the elements in the second subsequence. Since the result can be very large, return it modulo 10^9 + 7.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the input array.

**Return value**

- An integer representing the count of pairs of disjoint subsequences with equal GCD, modulo 10^9 + 7.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3]`
- Output: `5`
- Explanation: The pairs of subsequences are ([1], [1]), ([2], [2]), ([3], [3]), ([1, 2], [1, 2]), ([1, 3], [1, 3]).

**Example 2**

- Input: `nums = [10, 20, 30]`
- Output: `2`
- Explanation: The pairs are ([10], [10]), ([20], [20]), ([30], [30]), ([10, 20], [10, 20]), ([10, 30], [10, 30]), ([20, 30], [20, 30]), ([10, 20, 30], [10, 20, 30]). (Note: GCDs must match).

**Example 3**

- Input: `nums = [1, 1, 1, 1]`
- Output: `65`

---

## Underlying Base Algorithm(s)
The problem is solved using Dynamic Programming with state compression. We maintain a DP table `dp[g1][g2]` representing the number of ways to form two disjoint subsequences with GCDs `g1` and `g2` respectively. For each number `x` in the input, we update the DP table by considering three choices: adding `x` to the first subsequence, adding `x` to the second, or ignoring `x`. We use the property that the GCD of a subsequence is always a divisor of the elements within it, limiting the state space to the maximum value in `nums` (up to 200).

---

## Complexity Analysis
- **Time Complexity**: `O(N * M^2)`, where `N` is the length of the array and `M` is the maximum value in the array (200).
- **Space Complexity**: `O(M^2)` to store the DP table.
