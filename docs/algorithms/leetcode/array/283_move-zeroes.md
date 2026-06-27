# Move Zeroes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 283 |
| Difficulty | Easy |
| Topics | Array, Two Pointers |
| Official Link | [move-zeroes](https://leetcode.com/problems/move-zeroes/) |

## Problem Description & Examples
### Goal
Given an integer array, rearrange its elements such that all occurrences of zero are shifted to the end of the array while maintaining the relative order of the non-zero elements. This operation must be performed in-place, modifying the original array without creating a copy.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- `None`: The function modifies the input list `nums` in-place.

### Examples
**Example 1**

- Input: `[0, 1, 0, 3, 12]`
- Output: `[1, 3, 12, 0, 0]`

**Example 2**

- Input: `[0]`
- Output: `[0]`

**Example 3**

- Input: `[1, 2, 3]`
- Output: `[1, 2, 3]`

---

## Underlying Base Algorithm(s)
The Two-Pointer technique is used here. One pointer (`last_non_zero_index`) tracks the position where the next non-zero element should be placed, while the second pointer iterates through the array. By swapping elements, we effectively "bubble" the zeros to the back while preserving the sequence of non-zero integers.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the array, as we perform a single pass through the list.
- **Space Complexity**: `O(1)`, as the transformation is performed in-place using only a constant amount of extra space.
