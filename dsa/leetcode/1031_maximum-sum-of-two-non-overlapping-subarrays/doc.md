# Maximum Sum of Two Non-Overlapping Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1031 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/) |

## Problem Description

### Goal

Given an integer array `nums` and two lengths `firstLen` and `secondLen`, choose two non-overlapping subarrays: one with length `firstLen` and the other with length `secondLen`.

The `firstLen` subarray may appear before or after the `secondLen` subarray. Return the maximum possible sum of all elements in the two chosen subarrays.

A subarray is a contiguous part of the original array; elements cannot be skipped within either choice.

### Function Contract

**Inputs**

- `nums`: an array of $N$ integers, where `first_len + second_len <= len(nums) <= 1000` and $0 \le \texttt{nums[i]} \le 1000$.
- `first_len`: the length of one required subarray, where $1 \le \texttt{first_len} \le 1000$.
- `second_len`: the length of the other required subarray, where $1 \le \texttt{second_len} \le 1000$.
- The two lengths satisfy $2 \le \texttt{first_len}+\texttt{second_len} \le 1000$.

**Return value**

- The maximum combined sum of two non-overlapping subarrays with the specified lengths.

### Examples

**Example 1**

- Input: `nums = [0,6,5,2,2,5,1,9,4], first_len = 1, second_len = 2`
- Output: `20`
- Explanation: Choose `[9]` and `[6,5]`.

**Example 2**

- Input: `nums = [3,8,1,3,2,1,8,9,0], first_len = 3, second_len = 2`
- Output: `29`
- Explanation: Choose `[3,8,1]` and `[8,9]`.

**Example 3**

- Input: `nums = [2,1,5,6,0,9,5,0,3,8], first_len = 4, second_len = 3`
- Output: `31`
- Explanation: Choose `[5,6,0,9]` and `[0,3,8]`.
