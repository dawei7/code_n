# Sum of Good Subsequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3351 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-of-good-subsequences/) |

## Problem Description

### Goal

Given an integer array `nums`, consider every non-empty subsequence selected by indices in their original order. A subsequence is good when the absolute difference between each pair of consecutive selected values is exactly $1$. Every one-element subsequence is good because it has no consecutive pair to violate the condition.

For each good subsequence, compute the sum of all values it contains. Return the total of those sums across every possible good subsequence. Different index selections count separately even when they produce the same value sequence. Because the total can be large, return it modulo $10^9+7$.

### Function Contract

**Inputs**

- `nums`: A list of $n$ non-negative integers.

The source guarantees $1 \le n \le 10^5$ and $0 \le \texttt{nums[i]} \le 10^5$.

**Return value**

- Return the sum of the element sums of all good subsequences, modulo $10^9+7$.

### Examples

**Example 1**

- Input: `nums = [1, 2, 1]`
- Output: `14`
- Explanation: The good subsequences are the three singletons, `[1, 2]`, `[2, 1]`, and `[1, 2, 1]`. Their element sums total $1+2+1+3+3+4=14$.

**Example 2**

- Input: `nums = [3, 4, 5]`
- Output: `40`
- Explanation: The good subsequences are `[3]`, `[4]`, `[5]`, `[3, 4]`, `[4, 5]`, and `[3, 4, 5]`; their sums total $40$.

**Zero-value example**

- Input: `nums = [0, 1, 0]`
- Output: `4`
- Explanation: Zero-valued singletons contribute zero, while `[1]`, both index-distinct `[0, 1]` or `[1, 0]` pairs, and `[0, 1, 0]` produce a total contribution of four.
