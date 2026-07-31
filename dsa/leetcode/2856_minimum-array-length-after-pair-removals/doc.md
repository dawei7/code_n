# Minimum Array Length After Pair Removals

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2856 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Two Pointers, Binary Search, Greedy, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-array-length-after-pair-removals/) |

## Problem Description

### Goal

You are given an integer array `nums` sorted in non-decreasing order. In one operation, choose two indices `i` and `j` whose values satisfy `nums[i] < nums[j]`, then remove both selected elements. The surviving elements keep their relative order and are re-indexed.

You may perform this operation any number of times, including zero. Determine the minimum possible length of `nums` after choosing the removals optimally.

### Function Contract

**Inputs**

- `nums`: An integer array sorted in non-decreasing order.

Let $n = \lvert\texttt{nums}\rvert$. The constraints guarantee $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^9$.

**Return value**

The smallest number of elements that can remain after repeatedly removing pairs with strictly different values in increasing order.

### Examples

**Example 1**

- Input: `nums = [1, 2, 3, 4]`
- Output: `0`

All four elements can be divided into two valid unequal pairs.

**Example 2**

- Input: `nums = [1, 1, 2, 2, 3, 3]`
- Output: `0`

There is enough value diversity to remove every element.

**Example 3**

- Input: `nums = [1000000000, 1000000000]`
- Output: `2`

Equal values cannot form a removable pair.

**Example 4**

- Input: `nums = [2, 3, 4, 4, 4]`
- Output: `1`

Two copies of `4` can be paired with the two smaller values, leaving one element.
