# Number of Subsequences That Satisfy the Given Sum Condition

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1498 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Binary Search, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/) |

## Problem Description
### Goal

Given an integer array `nums` and an integer `target`, consider every non-empty subsequence of the array. A subsequence selects one or more original indices while preserving their relative order; equal values selected from different indices still form different choices.

Count the subsequences for which the sum of the selected minimum value and selected maximum value is less than or equal to `target`. Because the count can be very large, return it modulo $10^9+7$.

### Function Contract
**Inputs**

Let $N$ be the length of `nums`, and let $M=10^9+7$ be the result modulus.

- `nums`: an integer list with $1 \le N \le 10^5$.
- Every value satisfies $1 \le \texttt{nums[i]} \le 10^6$.
- `target`: an integer with $1 \le \texttt{target} \le 10^6$.

**Return value**

Return, modulo $M$, the number of non-empty subsequences whose minimum plus maximum is at most `target`.

### Examples
**Example 1**

- Input: `nums = [3,5,6,7], target = 9`
- Output: `4`
- Explanation: The valid subsequences are `[3]`, `[3,5]`, `[3,6]`, and `[3,5,6]`.

**Example 2**

- Input: `nums = [3,3,6,8], target = 10`
- Output: `6`
- Explanation: The two occurrences of `3` belong to different indices, so selections using either one are counted separately.

**Example 3**

- Input: `nums = [2,3,3,4,6,7], target = 12`
- Output: `61`
- Explanation: Of the $63$ non-empty subsequences, only `[7]` and `[6,7]` violate the condition.
