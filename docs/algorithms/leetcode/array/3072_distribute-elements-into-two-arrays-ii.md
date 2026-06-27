# Distribute Elements Into Two Arrays II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3072 |
| Difficulty | Hard |
| Topics | Array, Binary Indexed Tree, Segment Tree, Simulation |
| Official Link | [distribute-elements-into-two-arrays-ii](https://leetcode.com/problems/distribute-elements-into-two-arrays-ii/) |

## Problem Description & Examples
### Goal
Distribute elements from an input array into two separate arrays, `arr1` and `arr2`, based on the count of elements strictly greater than the current element. For each element `x` in the input, append it to `arr1` if the count of elements in `arr1` greater than `x` is greater than the count of elements in `arr2` greater than `x`. Otherwise, append it to `arr2`. If the counts are equal, prioritize `arr1`.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the sequence to be distributed.

**Return value**

- A list containing the concatenation of `arr1` and `arr2` after processing all elements.

### Examples
**Example 1**

- Input: `nums = [2, 1, 3, 3]`
- Output: `[2, 3, 1, 3]`

**Example 2**

- Input: `nums = [5, 14, 3, 1, 2]`
- Output: `[5, 3, 1, 2, 14]`

**Example 3**

- Input: `nums = [3, 3, 3, 3]`
- Output: `[3, 3, 3, 3]`

---

## Underlying Base Algorithm(s)
The problem requires efficient counting of elements greater than a value in a dynamic set. A **Binary Indexed Tree (BIT)** or **Fenwick Tree** is used to maintain frequency counts of elements. Since the values in `nums` can be large, we use **coordinate compression** (mapping unique values to their rank) to map the input range to a range suitable for the BIT index.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`, where `n` is the length of `nums`. Sorting for coordinate compression takes `O(n log n)`, and each of the `n` insertions/queries into the BIT takes `O(log n)`.
- **Space Complexity**: `O(n)` to store the BIT, the sorted unique values, and the two result arrays.
