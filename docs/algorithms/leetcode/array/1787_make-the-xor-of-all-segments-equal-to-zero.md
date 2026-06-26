# Make the XOR of All Segments Equal to Zero

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1787 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Dynamic Programming, Bit Manipulation, Counting |
| Official Link | [make-the-xor-of-all-segments-equal-to-zero](https://leetcode.com/problems/make-the-xor-of-all-segments-equal-to-zero/) |

## Problem Description & Examples
### Goal
Change as few values as possible so every length-`k` segment of the array has XOR equal to `0`.

### Function Contract
**Inputs**

- `nums`: a list of integers.
- `k`: the segment length.

**Return value**

Return the minimum number of changes needed.

### Examples
**Example 1**

- Input: `nums = [1,2,0,3,0], k = 1`
- Output: `3`

**Example 2**

- Input: `nums = [3,4,5,2,1,7,3,4,7], k = 3`
- Output: `3`

**Example 3**

- Input: `nums = [1,2,4,1,2,5,1,2,6], k = 3`
- Output: `3`

---

## Underlying Base Algorithm(s)
All positions with the same index modulo `k` must eventually form one chosen value group; the XOR of the `k` chosen group values must be zero. Count frequencies in each modulo class and run DP over possible XOR states, where changing a class to value `v` costs `class_size - frequency[v]`.

---

## Complexity Analysis
- **Time Complexity**: `O(k * X * U)`, where `X` is the XOR state range and `U` is distinct values per class
- **Space Complexity**: `O(X)`
