# Make Sum Divisible by P

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1590 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/make-sum-divisible-by-p/) |

## Problem Description
### Goal

Given an array of positive integers, remove one contiguous subarray so that the sum of the remaining elements is divisible by `p`. The removed subarray may be empty, so no removal is needed when the original sum is already divisible.

Minimize the number of removed elements. Removing the entire array is forbidden, even though that would leave a sum of zero. Return `-1` when no proper subarray can satisfy the divisibility condition.

### Function Contract
**Inputs**

- `nums`: An array of $N$ positive integers, where $1 \le N \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^9$.
- `p`: A divisor satisfying $1 \le p \le 10^9$.

**Return value**

Return the minimum length of a removable contiguous subarray, `0` if the total is already divisible by `p`, or `-1` if only removing the whole array could work.

### Examples
**Example 1**

- Input: `nums = [3,1,4,2], p = 6`
- Output: `1`

**Example 2**

- Input: `nums = [6,3,5,2], p = 9`
- Output: `2`

**Example 3**

- Input: `nums = [1,2,3], p = 3`
- Output: `0`
