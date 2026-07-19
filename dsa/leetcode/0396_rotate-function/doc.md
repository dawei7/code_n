# Rotate Function

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 396 |
| Difficulty | Medium |
| Topics | Array, Math, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/rotate-function/) |

## Problem Description
### Goal
Given an integer array of length $n$, consider all $n$ cyclic right rotations. For one rotated arrangement $B$, define its score as $F=\sum_{i=0}^{n-1} iB_i$.

Return the maximum score among the original arrangement and every right rotation. Negative values and scores are allowed, so the answer is not automatically zero. Compute successive scores from their relationship rather than rebuilding and rescoring every rotated array in quadratic time. The function returns only the greatest score, not the rotation count or arrangement that achieves it.

### Function Contract
**Inputs**

- `nums`: the integer array to rotate

**Return value**

- Return the greatest value of `sum(index * rotated[index])` over all `len(nums)` cyclic right rotations.

### Examples
**Example 1**

- Input: `nums = [4,3,2,6]`
- Output: `26`

**Example 2**

- Input: `nums = [100]`
- Output: `0`

**Example 3**

- Input: `nums = [1,2,3]`
- Output: `8`
