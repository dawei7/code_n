# Find the Maximum Length of Valid Subsequence I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3201 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming |
| Official Link | [find-the-maximum-length-of-valid-subsequence-i](https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/) |

## Problem Description & Examples
### Goal
Given an array of integers, determine the length of the longest subsequence such that the sum of every two consecutive elements in the subsequence is even. A subsequence is valid if all adjacent pairs sum to an even number, which mathematically implies that all elements in the subsequence must have the same parity (all even or all odd), or the subsequence must alternate between odd and even numbers.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- An integer representing the maximum length of a valid subsequence.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4]`
- Output: `4`
- Explanation: The subsequence `[1, 3]` (odd, odd) has length 2, `[2, 4]` (even, even) has length 2, and `[1, 2, 3, 4]` (odd, even, odd, even) has length 4. The maximum is 4.

**Example 2**

- Input: `nums = [1, 3, 5]`
- Output: `3`
- Explanation: The subsequence `[1, 3, 5]` consists of all odd numbers, so every adjacent pair sums to an even number.

**Example 3**

- Input: `nums = [0, 0, 0]`
- Output: `3`
- Explanation: The subsequence `[0, 0, 0]` consists of all even numbers.

---

## Underlying Base Algorithm(s)
The problem can be solved using a greedy counting approach. Since a valid subsequence requires either all elements to have the same parity or to alternate parities, we only need to track:
1. The count of all even numbers.
2. The count of all odd numbers.
3. The length of the longest alternating subsequence (starting with even or odd).

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we iterate through the list once.
- **Space Complexity**: `O(1)`, as we only use a few integer variables to store counts.
