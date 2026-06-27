# Next Permutation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 31 |
| Difficulty | Medium |
| Topics | Array, Two Pointers |
| Official Link | [next-permutation](https://leetcode.com/problems/next-permutation/) |

## Problem Description & Examples
### Goal
Given a sequence of integers, rearrange the numbers into the lexicographically next greater permutation. If such an arrangement is impossible (i.e., the sequence is sorted in descending order), transform the sequence into the lowest possible order (sorted in ascending order). The modification must be performed in-place using constant extra space.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`) representing the current permutation.

**Return value**

- `None`: The function modifies the input list `nums` in-place.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3]`
- Output: `nums = [1, 3, 2]`

**Example 2**

- Input: `nums = [3, 2, 1]`
- Output: `nums = [1, 2, 3]`

**Example 3**

- Input: `nums = [1, 1, 5]`
- Output: `nums = [1, 5, 1]`

---

## Underlying Base Algorithm(s)
The algorithm relies on the "Narayana Pandita" algorithm for generating permutations. It involves three steps:
1. Find the largest index `i` such that `nums[i] < nums[i + 1]`. If no such index exists, the array is in descending order; reverse the entire array.
2. If such an `i` exists, find the largest index `j` greater than `i` such that `nums[j] > nums[i]`.
3. Swap `nums[i]` and `nums[j]`, then reverse the sub-array starting from `i + 1` to the end of the list.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the array. We perform at most three linear passes over the array.
- **Space Complexity**: `O(1)`, as the transformation is performed in-place without using additional data structures.
