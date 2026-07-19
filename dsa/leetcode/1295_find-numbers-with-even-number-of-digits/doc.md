# Find Numbers with Even Number of Digits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1295 |
| Difficulty | Easy |
| Topics | Array, Math |
| Official Link | [LeetCode](https://leetcode.com/problems/find-numbers-with-even-number-of-digits/) |

## Problem Description
### Goal
Given an array `nums` of positive integers, inspect the ordinary decimal representation of every value. A number qualifies when its representation contains an even number of digits. For example, a two-digit or four-digit value qualifies, whereas a one-digit or three-digit value does not. The representations have no leading zeroes, so each value's magnitude determines its digit count unambiguously.

Return how many array elements qualify. Repeated values count separately because the question counts elements, not distinct integers.

### Function Contract
**Inputs**

- `nums`: an integer array of length $n$, where $1 \le n \le 500$ and $1 \le \texttt{nums[i]} \le 10^5$.

**Return value**

The number of indices whose value has two, four, or six decimal digits.

### Examples
**Example 1**

- Input: `nums = [12,345,2,6,7896]`
- Output: `2`
- Explanation: Only 12 and 7896 have even digit counts.

**Example 2**

- Input: `nums = [555,901,482,1771]`
- Output: `1`

**Example 3**

- Input: `nums = [10,100,1000]`
- Output: `2`
