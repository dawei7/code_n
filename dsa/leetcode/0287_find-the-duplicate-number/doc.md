# Find the Duplicate Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 287 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Binary Search, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-duplicate-number/) |

## Problem Description
### Goal
Given an array of $n + 1$ integers whose values all lie in the inclusive range `1..n`, exactly one distinct value occurs more than once. That duplicate may appear twice or several times, while every other value follows the input guarantee.

Return the duplicated value itself. Do not modify or sort the input array, and use only constant extra space. Meet the required subquadratic running time rather than comparing every pair. Treat array entries as values under the contract even though their bounded range also permits an implicit pointer structure; no missing value or duplicate index needs to be returned.

### Function Contract
**Inputs**

- `nums`: an array containing exactly one distinct duplicated value

**Return value**

The duplicated value.

### Examples
**Example 1**

- Input: `nums = [1,3,4,2,2]`
- Output: `2`

**Example 2**

- Input: `nums = [3,1,3,4,2]`
- Output: `3`

**Example 3**

- Input: `nums = [3,3,3,3,3]`
- Output: `3`
