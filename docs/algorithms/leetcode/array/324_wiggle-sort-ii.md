# Wiggle Sort II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 324 |
| Difficulty | Medium |
| Topics | Array, Divide and Conquer, Greedy, Sorting, Quickselect |
| Official Link | [wiggle-sort-ii](https://leetcode.com/problems/wiggle-sort-ii/) |

## Problem Description & Examples
### Goal
Given an integer array, rearrange the elements such that the sequence follows a "wiggle" pattern where `nums[0] < nums[1] > nums[2] < nums[3]...`. You are guaranteed that a valid wiggle sort arrangement always exists for any given input.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- `None`: The function should modify the input list `nums` in-place.

### Examples
**Example 1**

- Input: `nums = [1, 5, 1, 1, 6, 4]`
- Output: `[1, 4, 1, 5, 1, 6]` (Note: `[1, 6, 1, 5, 1, 4]` is also valid)

**Example 2**

- Input: `nums = [1, 3, 2, 2, 3, 1]`
- Output: `[2, 3, 1, 3, 1, 2]`

**Example 3**

- Input: `nums = [1, 1, 2, 2, 2, 1]`
- Output: `[1, 2, 1, 2, 1, 2]`

---

## Underlying Base Algorithm(s)
The optimal approach involves sorting the array and then partitioning it into two halves: the smaller half and the larger half. To satisfy the wiggle condition without collisions (especially with duplicate values), we fill the odd indices with the larger half and the even indices with the smaller half, both in reverse order. This ensures that the largest elements are placed far apart from each other.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)` due to the sorting step. While `O(n)` is possible using the Quickselect algorithm (Median of Medians), `O(n log n)` is the standard efficient approach.
- **Space Complexity**: `O(n)` to store the sorted copy of the array before rearranging it in-place.
