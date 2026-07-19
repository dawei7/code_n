# Delete and Earn

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 740 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/delete-and-earn/) |

## Problem Description
### Goal
Given an integer array `nums`, you may repeatedly choose one occurrence `nums[i]`, delete it, and earn `nums[i]` points. That choice also forces every remaining element equal to `nums[i] - 1` or `nums[i] + 1` to be deleted without earning their points.

Return the maximum total points obtainable through any sequence of choices. Other occurrences equal to the chosen value are not removed by that rule and may be selected for additional points, while choosing one value makes its two immediately adjacent values unavailable wherever they occur.

### Function Contract
**Inputs**

- `nums`: a nonempty list of positive integers

**Return value**

- The greatest total obtainable when choosing a number `x` earns `x` and removes every remaining occurrence of `x-1` and `x+1`

### Examples
**Example 1**

- Input: `nums = [3,4,2]`
- Output: `6`

**Example 2**

- Input: `nums = [2,2,3,3,3,4]`
- Output: `9`

**Example 3**

- Input: `nums = [10,10,9,9,11]`
- Output: `29`
