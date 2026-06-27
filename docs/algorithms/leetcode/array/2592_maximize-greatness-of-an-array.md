# Maximize Greatness of an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2592 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Greedy, Sorting |
| Official Link | [maximize-greatness-of-an-array](https://leetcode.com/problems/maximize-greatness-of-an-array/) |

## Problem Description & Examples
### Goal
Given an array of integers, rearrange its elements to form a permutation such that the number of indices `i` where the new element is strictly greater than the original element at that index is maximized. Return this maximum count.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- An integer representing the maximum number of indices where the permuted array elements are strictly greater than the original elements.

### Examples
**Example 1**

- Input: `nums = [1,3,5,2,1,3,1]`
- Output: `4`

**Example 2**

- Input: `nums = [1,2,3,4]`
- Output: `3`

**Example 3**

- Input: `nums = [10,10,10]`
- Output: `0`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Greedy approach combined with Sorting**. By sorting the array, we can efficiently pair the smallest available elements with the smallest possible elements that are strictly greater than them. A **Two Pointers** technique is used to traverse the sorted array: one pointer tracks the "target" (the element we want to beat) and the other tracks the "candidate" (the element we use to beat the target).

---

## Complexity Analysis
- **Time Complexity**: `O(N log N)` due to the sorting step, where `N` is the length of the input array. The subsequent two-pointer traversal is `O(N)`.
- **Space Complexity**: `O(1)` or `O(N)` depending on the sorting implementation's space requirements (Python's Timsort is `O(N)`).
