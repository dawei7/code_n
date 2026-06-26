# Maximum of Absolute Value Expression

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1131 |
| Difficulty | Medium |
| Topics | Array, Math |
| Official Link | [maximum-of-absolute-value-expression](https://leetcode.com/problems/maximum-of-absolute-value-expression/) |

## Problem Description & Examples
### Goal
For arrays `arr1` and `arr2`, maximize `|arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|` over all valid indices.

### Function Contract
**Inputs**

- `arr1`: first integer array.
- `arr2`: second integer array of the same length.

**Return value**

The maximum expression value.

### Examples
**Example 1**

- Input: `arr1 = [1,2,3,4]`, `arr2 = [-1,4,5,6]`
- Output: `13`

**Example 2**

- Input: `arr1 = [1,-2,-5,0,10]`, `arr2 = [0,-2,-1,-7,-4]`
- Output: `20`

**Example 3**

- Input: `arr1 = [0,0]`, `arr2 = [0,1]`
- Output: `2`

---

## Underlying Base Algorithm(s)
Sign expansion of absolute values.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
