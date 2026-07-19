# Maximum Product Subarray

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 152 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-product-subarray/) |

## Problem Description
### Goal
Given a nonempty list of integers, choose a contiguous subarray containing at least one element and multiply all values in that interval. The interval may begin and end anywhere but cannot skip elements or combine separated portions of the input.

Return the largest product obtainable over all such intervals. Negative values matter because two negative factors can turn a small or negative running product into a large positive one, while zero splits products and is itself a valid one-element result. The chosen interval is not returned. When every longer product is worse, a single input value may supply the answer.

### Function Contract
**Inputs**

- `nums`: a nonempty list of integers

**Return value**

The maximum product among all contiguous subarrays.

### Examples
**Example 1**

- Input: `nums = [2,3,-2,4]`
- Output: `6`

**Example 2**

- Input: `nums = [-2,0,-1]`
- Output: `0`

**Example 3**

- Input: `nums = [-2,3,-4]`
- Output: `24`
