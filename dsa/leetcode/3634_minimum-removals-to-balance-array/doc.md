# Minimum Removals to Balance Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3634 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Sliding Window, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-removals-to-balance-array/) |

## Problem Description

### Goal

You are given an integer array `nums` and an integer `k`. A nonempty array is balanced when its maximum value is at most `k` times its minimum value.

Remove any number of elements while leaving at least one element. Return the fewest removals needed for the remaining values to be balanced. A single remaining element is always balanced because its minimum and maximum are equal.

### Function Contract

**Inputs**

- `nums`: A list of $n$ positive integers, where $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^9$.
- `k`: A positive multiplier satisfying $1 \le \texttt{k} \le 10^5$.

**Return value**

Return the minimum number of elements that must be removed so the nonempty remainder satisfies $\max \le k\min$.

### Examples

#### Example 1

- **Input:** `nums = [2, 1, 5], k = 2`
- **Output:** `1`
- **Explanation:** Removing 5 leaves minimum 1 and maximum 2, and $2\le2\times1$.

#### Example 2

- **Input:** `nums = [1, 6, 2, 9], k = 3`
- **Output:** `2`
- **Explanation:** Keeping 2 and 6 gives $6\le3\times2$.

#### Example 3

- **Input:** `nums = [4, 6], k = 2`
- **Output:** `0`
- **Explanation:** The original array already satisfies $6\le2\times4$.
