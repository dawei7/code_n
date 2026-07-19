# Majority Element II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 229 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Sorting, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/majority-element-ii/) |

## Problem Description
### Goal
Given a nonempty integer array of length `n`, identify every distinct value whose frequency is strictly greater than $\left\lfloor n / 3 \right\rfloor$. Occurrences may appear anywhere in the array, and no more than two distinct values can satisfy this threshold.

Return all qualifying values in any order, listing each value once regardless of its frequency. A value occurring exactly one third of the time does not qualify. Negative integers and zero are treated normally. Meet the follow-up target of linear time and $O(1)$ space rather than returning a complete frequency table or sorting a copied array.

### Function Contract
**Inputs**

- `nums`: a non-empty list of integers

**Return value**

A list containing every value whose frequency is greater than `len(nums) / 3`, in any order.

### Examples
**Example 1**

- Input: `nums = [3, 2, 3]`
- Output: `[3]`

**Example 2**

- Input: `nums = [1]`
- Output: `[1]`

**Example 3**

- Input: `nums = [1, 2]`
- Output: `[1, 2]`
