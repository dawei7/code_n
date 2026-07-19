# Three Equal Parts

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 927 |
| Difficulty | Hard |
| Topics | Array, Math |
| Official Link | [LeetCode](https://leetcode.com/problems/three-equal-parts/) |

## Problem Description
### Goal

You are given a binary array `arr`. Divide the entire array into three non-empty contiguous parts whose binary values are equal. Return any pair `[i, j]` with `i + 1 < j`: the first part is `arr[0]` through `arr[i]`, the second is `arr[i + 1]` through `arr[j - 1]`, and the third is `arr[j]` through the final element.

Every bit in a part contributes to its binary representation. Thus `[1,1,0]` represents six rather than three. Leading zeros are permitted and do not change a part's value, so parts such as `[0,1,1]` and `[1,1]` are equal. If no valid pair of cuts exists, return `[-1,-1]`.

### Function Contract
**Inputs**

- `arr`: an array of $n$ bits, where $3\le n\le3\cdot10^4$ and every element is `0` or `1`.

**Return value**

Any `[i, j]` that creates three non-empty parts with equal binary values and satisfies `i + 1 < j`, or `[-1,-1]` when no such partition exists.

### Examples
**Example 1**

- Input: `arr = [1,0,1,0,1]`
- Output: `[0,3]`

**Example 2**

- Input: `arr = [1,1,0,1,1]`
- Output: `[-1,-1]`

**Example 3**

- Input: `arr = [1,1,0,0,1]`
- Output: `[0,2]`
