# Maximum Product of Three Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 628 |
| Difficulty | Easy |
| Topics | Array, Math, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-product-of-three-numbers/) |

## Problem Description
### Goal
Given an integer array `nums` containing at least three values, choose three numbers from three distinct array positions and multiply them together. Negative values and zero may appear, so the three numerically largest values do not always produce the greatest product.

Return the maximum product obtainable from any such choice of three numbers. Each array occurrence can be used at most once, while equal values at different positions remain separate selectable numbers.

### Function Contract
**Inputs**

- `nums`: an integer list containing at least three values

**Return value**

- The maximum product obtainable from values at three distinct indices

### Examples
**Example 1**

- Input: `nums = [1,2,3]`
- Output: `6`

**Example 2**

- Input: `nums = [1,2,3,4]`
- Output: `24`

**Example 3**

- Input: `nums = [-10,-10,5,2]`
- Output: `500`
