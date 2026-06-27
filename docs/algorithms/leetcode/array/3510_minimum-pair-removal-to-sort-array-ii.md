# Minimum Pair Removal to Sort Array II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3510 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Linked List, Heap (Priority Queue), Simulation, Doubly-Linked List, Ordered Set |
| Official Link | [minimum-pair-removal-to-sort-array-ii](https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/) |

## Problem Description & Examples
### Goal
Given an array of integers, you are permitted to remove adjacent pairs of elements if they satisfy a specific condition (typically related to non-decreasing order or parity). The objective is to determine the minimum number of removals required to transform the remaining elements into a non-decreasing sequence. If it is impossible to sort the array through these removals, return -1.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the sequence to be processed.

**Return value**

- An integer representing the minimum number of pair removals needed to make the array sorted, or -1 if it is impossible.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4]`
- Output: `0`

**Example 2**

- Input: `nums = [5, 1, 2, 3]`
- Output: `1`

**Example 3**

- Input: `nums = [3, 2, 1]`
- Output: `-1`

---

## Underlying Base Algorithm(s)
The problem is solved using a Greedy approach combined with a Monotonic Stack or a Doubly-Linked List to simulate the removal process. By identifying "inversions" (where `nums[i] > nums[i+1]`), we prioritize removing elements that violate the sorted property. A Priority Queue (Heap) is often used to track the indices of these violations to ensure we perform the minimum number of operations.

---

## Complexity Analysis
- **Time Complexity**: `O(N log N)`, where `N` is the length of the array, due to the use of a heap to manage potential removal candidates.
- **Space Complexity**: `O(N)` to store the array structure and the heap of indices.
