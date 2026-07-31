# Sum of Consecutive Subsequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3299 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-of-consecutive-subsequences/) |

## Problem Description

### Goal

A non-empty array is consecutive when every adjacent difference is $1$, or when every adjacent difference is $-1$. The direction must remain the same throughout: `[3,4,5]` and `[9,8]` qualify, whereas `[3,4,3]` and `[8,6]` do not. Every one-element array is consecutive.

Given `nums`, consider every non-empty subsequence obtained by retaining elements in their original relative order. The value of a qualifying subsequence is the sum of its elements. Add the values of all consecutive subsequences, counting different choices of indices separately, and return the result modulo $10^9+7$.

### Function Contract

**Inputs**

- `nums`: A list of positive integers from which non-empty subsequences are selected.

The list length and every element value are each from 1 through $10^5$.

**Return value**

- The sum of the element sums of all consecutive non-empty subsequences, reduced modulo $10^9+7$.

### Examples

**Example 1**

- Input: `nums = [1,2]`
- Output: `6`
- Explanation: The qualifying subsequences are `[1]`, `[2]`, and `[1,2]`, with values 1, 2, and 3.

**Example 2**

- Input: `nums = [1,4,2,3]`
- Output: `31`
- Explanation: Besides the four singletons, the qualifying choices are `[1,2]`, `[2,3]`, `[4,3]`, and `[1,2,3]`.

**Example 3**

- Input: `nums = [3,2,1]`
- Output: `20`
- Explanation: All three singletons, both adjacent-value pairs, and `[3,2,1]` are decreasing consecutive subsequences.
