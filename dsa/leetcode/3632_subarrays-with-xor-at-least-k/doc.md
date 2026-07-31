# Subarrays with XOR at Least K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3632 |
| Difficulty | Hard |
| Topics | Array, Bit Manipulation, Trie, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/subarrays-with-xor-at-least-k/) |

## Problem Description
### Goal

Given an integer array `nums` and a non-negative integer `k`, consider every contiguous subarray. The value of a subarray is the bitwise XOR of all elements from its left endpoint through its right endpoint.

Count and return how many of those subarrays have XOR greater than or equal to `k`. Endpoints distinguish subarrays, so equal sequences appearing at different positions are counted separately.

### Function Contract
**Inputs**

- `nums`: A list of $n$ integers, where $1 \le n \le 10^5$ and $0 \le \texttt{nums[i]} \le 10^9$.
- `k`: A threshold satisfying $0 \le \texttt{k} \le 10^9$.

**Return value**

Return the number of contiguous subarrays whose bitwise XOR is at least `k`.

### Examples
**Example 1**

- Input: `nums = [3, 1, 2, 3], k = 2`
- Output: `6`
- Explanation: Six endpoint pairs produce XOR 2 or greater, including each singleton 3 and the singleton 2.

**Example 2**

- Input: `nums = [0, 0, 0], k = 0`
- Output: `6`
- Explanation: All $3\times4/2=6$ nonempty subarrays have XOR zero, which meets the inclusive threshold.
