# Remove One Element to Make the Array Strictly Increasing

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/) |
| Frontend ID | 1909 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

You are given a 0-indexed integer array `nums`. Remove exactly one element, keeping every other element in its original relative order, and decide whether the resulting array can be strictly increasing.

An array is strictly increasing when every element after the first is greater than its immediate predecessor. If `nums` already has this property, return `True`: removing its first or last element leaves a shorter strictly increasing array.

### Function Contract

**Inputs**

- `nums`: a list of $N$ integers.
- $2 \le N \le 1000$.
- $1 \le \texttt{nums[i]} \le 1000$.

**Return value**

- Return `True` if removing exactly one element can leave a strictly increasing array; otherwise return `False`.

### Examples

**Example 1**

- Input: `nums = [1,2,10,5,7]`
- Output: `True`

Removing `10` leaves `[1,2,5,7]`.

**Example 2**

- Input: `nums = [2,3,1,2]`
- Output: `False`

No single removal repairs both order conflicts.

**Example 3**

- Input: `nums = [1,1,1]`
- Output: `False`

Every possible result is `[1,1]`, which is not strictly increasing.
