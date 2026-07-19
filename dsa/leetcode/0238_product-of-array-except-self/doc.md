# Product of Array Except Self

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 238 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/product-of-array-except-self/) |

## Problem Description
### Goal
Given an integer array `nums` of at least two elements, construct an output of the same length. At each index `i`, the output value must equal the product of every input element except `nums[i]` itself. The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

Return all position-specific products without using division, and compute them in linear time. Zero values follow the same rule: one zero makes every other position's product zero, while two or more zeroes make all products zero. The output array does not count toward the constant-extra-space target, but do not allocate additional storage that grows with the input beyond that returned result.

### Function Contract
**Inputs**

- `nums`: a list of at least two integers

**Return value**

A list where position `i` contains the product of every `nums[j]` for which $j \ne i$.

### Examples
**Example 1**

- Input: `nums = [1,2,3,4]`
- Output: `[24,12,8,6]`

**Example 2**

- Input: `nums = [-1,1,0,-3,3]`
- Output: `[0,0,9,0,0]`

**Example 3**

- Input: `nums = [2,3]`
- Output: `[3,2]`
