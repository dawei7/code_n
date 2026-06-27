# Divide Array Into Arrays With Max Difference

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2966 |
| Difficulty | Medium |
| Topics | Array, Greedy, Sorting |
| Official Link | [divide-array-into-arrays-with-max-difference](https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/) |

## Problem Description & Examples
### Goal
Given an array of integers, partition the elements into groups of three such that the difference between the maximum and minimum element in each group is at most a specified threshold `k`. If it is impossible to partition all elements according to this constraint, return an empty array.

### Function Contract
**Inputs**

- `nums`: A list of integers where the length is a multiple of 3.
- `k`: An integer representing the maximum allowed difference within any triplet.

**Return value**

- A list of lists containing the partitioned triplets if a valid partition exists; otherwise, an empty list.

### Examples
**Example 1**

- Input: `nums = [1,3,4,8,7,9,3,5,1], k = 2`
- Output: `[[1,1,3],[3,4,5],[7,8,9]]`

**Example 2**

- Input: `nums = [1,3,3,2,7,3], k = 3`
- Output: `[]`

**Example 3**

- Input: `nums = [2,4,2,7,8,8], k = 2`
- Output: `[]`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Greedy approach combined with Sorting**. By sorting the array first, we ensure that for any triplet `(a, b, c)` where `a <= b <= c`, the difference `c - a` is minimized. If the difference between the first and third element of any consecutive triplet in the sorted array exceeds `k`, then no valid partition exists.

---

## Complexity Analysis
- **Time Complexity**: `O(N log N)`, where `N` is the number of elements in the input array, due to the sorting step. The subsequent linear scan takes `O(N)`.
- **Space Complexity**: `O(N)` to store the resulting triplets.
